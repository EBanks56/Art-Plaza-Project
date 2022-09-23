from flask import render_template, request, redirect, session
from flask_app import app
from flask import flash
from flask_app.models.purchase import Purchase
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect ('/login')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/process', methods=['POST'])
def process():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/home')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/register')
    if not User.user_exist(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "full_name": request.form["full_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/create_profile')

@app.route('/home')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("home.html", user=User.get_one(data), posts=Post.get_all_posts())

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/login')