from apps.models import *
from config import *
from flask import render_template, Blueprint, session, request
from .auth import authenticated

profil_route = Blueprint("profil_route", __name__)


@profil_route.route("/profil/<int:id>", methods=["GET", "POST"])
@authenticated(["user"])
def profil(id):
    query_result = db.session.query(Users).filter(Users.id == id).one()

    if request.method == "POST":
        print("test")
        print(request.form)
        query_result.surname = request.form["surname"]
        query_result.name = request.form["name"]
        db.session.commit()

    render_data = {
        "show_user": query_result,
        "current_user": db.session.query(Users)
        .filter(Users.id == session["user_id"])
        .one(),
        "BASE_PATH": BASE_PATH,
    }
    return render_template("profil.html", **render_data)
