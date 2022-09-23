from flask import render_template, request, redirect, session
from flask_app import app
from flask import flash
from flask_app.models.user import User
from flask_app.models.profile import Profile

@app.route('/create_profile')
def newProfile():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('create_profile.html', user=User.get_one(data))

@app.route('/create/profile', methods = ['POST'])
def createProfile():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Profile.validate_profile(request.form):
        return redirect('/create_profile')
    data = {
        'username': request.form['username'],
        'location': request.form['location'],
        'contact': request.form['contact'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Profile.save(data)
    return redirect('/home')

@app.route('/edit/profile/<int:user_id>')
def editProfile(user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": user_id
    }
    return render_template("edit_profile.html", profile=Profile.get_profile(data))

@app.route('/update/profile', methods=['POST'])
def updateProfile():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Profile.validate_profile(request.form):
        return redirect('/create_profile')
    data = {
        'username': request.form['username'],
        'location': request.form['location'],
        'contact': request.form['contact'],
        'description': request.form['description'],
        'id': request.form['id'],
    }
    Profile.update(data)
    return redirect('/home')

@app.route('/view/profile/<int:user_id>')
def showProfile(user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": user_id
    }
    return render_template("profile.html", profile=Profile.get_profile(data))