from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import post
from flask_app.models import user

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.totalLikes = 0

    @classmethod
    def save(cls, data):
        query = "INSERT INTO likes (user_id, post_id) VALUES (%(user_id)s, %(post_id)s);"
        return connectToMySQL('art plaza').query_db(query,data)

    @classmethod
    def total_likes(cls, data):
        query = "SELECT * FROM posts LEFT JOIN likes ON likes.post_id = posts.id WHERE posts.id = %(id)s"
        results = connectToMySQL('art plaza').query_db(query, data)
        like = cls(results[0])
        for i in results:
            like.totalLikes += 1
            print(i)
        return like

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM likes WHERE post_id=%(post_id)s and user_id = %(user_id)s"
        return connectToMySQL('art plaza').query_db(query,data)

    @classmethod
    def like_exist(cls, data):
        is_valid = False
        query = "SELECT * FROM likes WHERE post_id=%(post_id)s and user_id = %(user_id)s;"
        results = connectToMySQL('art plaza').query_db(query, data)
        if len(results) > 0:
            flash("You already liked this series.")
            is_valid = True
        return is_valid