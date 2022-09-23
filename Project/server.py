from flask_app.controllers import users
from flask_app.controllers import posts
from flask_app.controllers import purchases
from flask_app.controllers import likes
from flask_app.controllers import profiles
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)