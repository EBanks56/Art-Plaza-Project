from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.purchase import Purchase

@app.route('/purchase/<int:post_id>', methods = ['POST'])
def purchase(post_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": session['user_id'],
        "post_id": post_id
    }
    if Purchase.purchase_exist(data):
        return redirect('/home')
    Purchase.save(data)
    return redirect('/purchases')

@app.route('/purchases')
def user_purchases():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("purchases.html", purchases=Purchase.get_all_purchases(data), user=User.get_one(data))

@app.route('/cancel/<int:id>')
def cancelPurchase(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Purchase.delete(data)
    return redirect('/home')