from apps.models import *
from flask import render_template, Blueprint, session, request
from .auth import authenticated
from apps.exceptions import EmailAddressExists
from random import getrandbits

admin_route = Blueprint("admin_route", __name__)


@admin_route.route("/admin/", methods=["GET", "POST"])
@authenticated(["admin"])
def admin():
    error = []
    if request.method == "POST":
        print("[DEBUG]", "#1")
        if "email" in request.form:
            surname, name, email = (
                request.form["surname"],
                request.form["name"],
                request.form["email"],
            )
            if surname and name and email:
                try:
                    if (
                        db.session.query(Users)
                        .filter(Users.email == request.form["email"])
                        .first()
                        == None
                    ):
                        Users(
                            surname=surname,
                            name=name,
                            email=email,
                        ).insert()

                        print(getToken())

                        UserRegister(
                            userId=db.session.query(Users)
                            .filter(Users.email == email)
                            .first()
                            .id,
                            token=getToken(),
                        ).insert()

                    else:
                        raise EmailAddressExists
                except EmailAddressExists:
                    error.append("Email existiert bereits!")

    render_data = {
        "current_user": db.session.query(Users)
        .filter(Users.id == session["user_id"])
        .one(),
        "errors": error,
    }

    return render_template("admin.html", **render_data)


def getToken():
    token = hex(getrandbits(256))[2:]

    if (
        db.session.query(UserRegister).filter(UserRegister.token == token).first()
        == None
    ):
        return token
    else:
        return getToken()
