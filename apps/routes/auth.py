from apps.models import *
from flask import render_template, Blueprint, request, session

auth_route = Blueprint('auth_route', __name__)


@auth_route.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        if request.form["submit_button"] == "sub":
            var = 1
        return render_template("login.html", **renderdata)
    elif request.method == "GET":
        renderdata = {"var": var}
        return render_template("login.html", **renderdata)

@auth_route.route("/register/")
def register():

    renderdata = {"email": session["email"],
                  "password": session["password"]}
    
    return render_template("register.html", **renderdata)

@auth_route.route("/logout")
def logout():
    
    return "logout"
