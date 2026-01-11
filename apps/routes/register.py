from apps.models import *
from config import *
from flask import render_template, Blueprint, session, request

register_route = Blueprint("register_route", __name__)


@register_route.route("/register/", methods=["GET", "POST"])
def register():
    token = request.args.get("token")

    render_data = {
        "user": db.session.query(Users)
        .filter(
            Users.id
            == db.session.query(UserRegister)
            .filter(UserRegister.token == token)
            .one()
            .userId
        )
        .one(),
        "token": token,
        "BASE_PATH": BASE_PATH,
    }
    return render_template("register.html", **render_data)
