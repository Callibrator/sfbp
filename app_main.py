#This is the main API File... it binds together all the functions and makes the program run!


#Importing my own directories that contain my functions.
import sys

sys.path.append("./pages")
sys.path.append("./config")

#Importing Modules
from flask import Flask
from flask import redirect,session
from flask_login import LoginManager
import config


#Pages
from index_page import index_page


app = Flask(__name__)
app.secret_key = config.app_secret_key


#Registering Pages
app.register_blueprint(index_page)

#app.register_blueprint(login_page)



# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# @login_manager.unauthorized_handler
# def unaothorized():
#     return redirect("/login")
#
# @login_manager.user_loader
# def load_user(user_id):
#     cnx = getDatabaseConnector()
#     db = cnx.cursor()
#     data = getUserById(db,user_id)
#     if data == None:
#         session.clear()
#         return None
#     id = data["id"]
#     uname = data["username"]
#     u = User(uname,id)
#
#     db.close()
#     cnx.close()
#     return u


#Running the APP
if __name__ == "__main__":
    app.run()