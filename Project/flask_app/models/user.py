from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models import post
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (full_name, email, password) VALUES (%(full_name)s, %(email)s, %(password)s);"
        return connectToMySQL('art plaza').query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['full_name']) < 2:
            flash("Name must be over 2 characters.")
            is_valid = False
        if len(user['email']) == 0:
            flash("Email cannot be blank.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be over 8 characters.")
            is_valid = False
        if (user['confirm-password']) != (user['password']):
            flash("Password doesn't match.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        return is_valid

    @staticmethod
    def user_exist(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('art plaza').query_db(query, user)
        if len(results) > 1:
            flash("Email already taken.")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('art plaza').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('art plaza').query_db(query,data)
        return cls(results[0])