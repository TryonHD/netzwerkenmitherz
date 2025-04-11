from apps.models import *
from flask import render_template, Blueprint

auth_route = Blueprint('auth_route', __name__)

@auth_route.route("/login/")
def login():

    return render_template("login.html")

@auth_route.route("/register/")
def register():

    return render_template("register.html")

@auth_route.route("/logout")
def logout():
    
    return "logout"
