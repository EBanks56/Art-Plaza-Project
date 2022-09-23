from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.like import Like

@app.route('/like/<int:post_id>', methods=['POST'])
def like_series(post_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": session['user_id'],
        "post_id": post_id
    }
    if Like.like_exist(data):
        return redirect('/home')
    Like.save(data)
    return redirect('/home')

@app.route('/unlike/<int:post_id>')
def unlike_series(post_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": session['user_id'],
        "post_id": post_id
    }
    Like.delete(data)
    return redirect('/home')