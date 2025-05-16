from apps.models import *
from flask import render_template, redirect, Blueprint, request, session, abort
from hashlib import sha256
from sqlalchemy.orm import exc
from apps.exceptions import PasswordNotMatched

auth_route = Blueprint('auth_route', __name__)

def authenticated(roles: list):
    def wrapper(f):
        def decorated(*args, **kwargs):
            user_roles = session.get("user_roles", None)
            if user_roles:
                if "admin" in user_roles:
                    return f(*args, **kwargs)
                for role in roles:
                    if role in user_roles:
                        return f(*args, **kwargs)
            return abort(404)
        return decorated
    return wrapper

@auth_route.route("/login/", methods=["GET", "POST"])
def login():
    var = 0
    if request.method == "POST":
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        if email and password:
            password = sha256(password.encode("utf-8")).hexdigest()

            try:
                user = db.session.query(Users).filter(Users.email == email).one()
                if user.password == password:
                    session["user_id"] = user.id
                    session['user_roles'] = [ x.role.name for x in user.user_roles ]
                    return redirect("/")
                else:
                        raise PasswordNotMatched
            except exc.NoResultFound:
                return render_template("login.html", error_msg="Email oder Passwort ist falsch!")
            except exc.MultipleResultsFound:
                return render_template("login.html", error_msg="Bitte kontaktieren sie ihren Administrator!")
            except PasswordNotMatched:
                return render_template("login.html", error_msg="Email oder Passwort ist falsch!")

            return {"status": True}
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
