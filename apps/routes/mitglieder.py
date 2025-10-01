from apps.models import *
from flask import render_template, Blueprint, session
from .auth import authenticated

mitglieder_route = Blueprint("mitglieder_route", __name__)


@mitglieder_route.route("/mitglieder/")
@authenticated
def mitglieder(user_id):
    render_data = {
        "current_user": db.session.query(Users)
        .filter(Users.id == session["user_id"])
        .one(),
    }
    return render_template("mitglieder.html", **render_data)
