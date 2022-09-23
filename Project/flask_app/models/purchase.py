from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import post
from flask_app.models import user

class Purchase:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.postImage = data['postImage']
        self.postName = data['postName']
        self.postDescription = data['postDescription']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO purchases (user_id, post_id) VALUES (%(user_id)s, %(post_id)s);"
        return connectToMySQL('art plaza').query_db(query, data)

    @classmethod
    def get_all_purchases(cls, data):
        query = "SELECT posts.image as postImage, posts.name as postName, posts.description AS postDescription, purchases.* FROM users JOIN purchases ON purchases.user_id = users.id JOIN posts ON purchases.post_id = posts.id WHERE purchases.user_id = %(id)s;"
        results = connectToMySQL('art plaza').query_db(query, data)
        all_purchases= []
        for row in results:
            all_purchases.insert(0, cls(row))
        return all_purchases

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM purchases WHERE id=%(id)s"
        return connectToMySQL('art plaza').query_db(query,data)

    @classmethod
    def purchase_exist(cls, data):
        is_valid = False
        query = "SELECT * FROM purchases WHERE post_id=%(post_id)s;"
        results = connectToMySQL('art plaza').query_db(query, data)
        if len(results) > 0:
            flash("This artwork has already been purchased. Check Re")
            is_valid = True
        return is_valid
