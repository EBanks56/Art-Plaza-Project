from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = data['creator']
        self.likes = 0

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (name, description, price, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(price)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('art plaza').query_db(query, data)

    @classmethod
    def get_all_posts(cls):
        query = "SELECT users.full_name as creator, posts.* FROM users JOIN posts ON users.id = posts.user_id;"
        results = connectToMySQL('art plaza').query_db(query)
        all_posts = []
        for row in results:
            all_posts.insert(0, cls(row))
        return all_posts

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT users.full_name as creator, posts.* FROM users JOIN posts ON users.id = posts.user_id WHERE posts.id = %(id)s;"
        results = connectToMySQL('art plaza').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET name=%(name)s, description=%(description)s, price=%(price)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL('art plaza').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE posts, likes, purchases FROM posts LEFT JOIN likes ON likes.post_id = posts.id LEFT JOIN purchases ON purchases.post_id = posts.id WHERE posts.id=%(id)s"
        return connectToMySQL('art plaza').query_db(query,data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['name']) < 2:
            flash("'Post Name' must be over 2 characters.")
            is_valid = False
        if len(post['description']) < 1:
            flash("'Post Description' field is required.")
            is_valid = False
        if post['price'] == '' or int(post['price']) < 1 or int(post['price']) > 2147483647:
            flash("'Post Price' must not be left empty. Must be between $1 and $2147483647.")
            is_valid = False
        return is_valid