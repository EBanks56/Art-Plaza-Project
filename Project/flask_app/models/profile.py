from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Profile:
    def __init__(self, data):
        self.profile_pic = data['profile_pic']
        self.username = data['username']
        self.location = data['location']
        self.contact = data['contact']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.profileCreator = data['profileCreator']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO profiles (username, location, contact, description, created_at, updated_at, user_id) VALUES (%(username)s, %(location)s, %(contact)s, %(description)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('art plaza').query_db(query, data)

    @staticmethod
    def validate_profile(profile):
        is_valid = True
        if len(profile['username']) < 2:
            flash("username must be over 2 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def username_exist(profile):
        is_valid = True
        query = "SELECT * FROM profiles WHERE username = %(username)s;"
        results = connectToMySQL('art plaza').query_db(query, profile)
        if len(results) > 1:
            flash("username already taken.")
            is_valid = False
        return is_valid

    @classmethod
    def get_profile(cls, data):
        query = "SELECT users.full_name as profileCreator, profiles.* FROM users JOIN profiles ON users.id = profiles.user_id WHERE user_id = %(user_id)s;"
        results = connectToMySQL('art plaza').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE profiles SET username=%(username)s, location=%(location)s, contact=%(contact)s, description=%(description)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL('art plaza').query_db(query, data)