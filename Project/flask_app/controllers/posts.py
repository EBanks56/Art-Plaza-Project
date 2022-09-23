from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.like import Like

@app.route('/new/post')
def newPost():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('create_post.html', user=User.get_one(data))

@app.route('/create/post', methods = ['POST'])
def createPost():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price'],
        'user_id': session['user_id']
    }
    Post.save(data)
    return redirect('/home')

@app.route('/edit/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("edit_post.html", post=Post.get_one_with_user(data), user=User.get_one(user_data))

@app.route('/update/post', methods=['POST'])
def update_car():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price'],
        'id': request.form['id']
    }
    Post.update(data)
    return redirect('/home')

@app.route('/view/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    return render_template("post.html", post=Post.get_one_with_user(data), likes=Like.total_likes(data))

@app.route('/delete/<int:id>')
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Post.delete(data)
    return redirect('/home')