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
        print("[Debug]")
        print(request.form)
        if "name" in request.form:
            query_result.surname = request.form["surname"]
            query_result.name = request.form["name"]
            db.session.commit()
        if "company_name" in request.form:
            query_result.company.name = request.form["company_name"]
            db.session.commit()
        if "street" in request.form:
            query_result.company.street = request.form["street"]
            query_result.company.housenumber = request.form["housenumber"]
            query_result.company.postalcode = request.form["postalcode"]
            query_result.company.city = request.form["city"]
            db.session.commit()
        if "email" in request.form:
            query_result.email = request.form["email"]
            query_result.phonenumber = request.form["phonenumber"]
            db.session.commit()
        if "description" in request.form:
            query_result.company.description = request.form["description"]
            db.session.commit()

    render_data = {
        "show_user": query_result,
        "current_user": db.session.query(Users)
        .filter(Users.id == session["user_id"])
        .one(),
        "BASE_PATH": BASE_PATH,
    }
    return render_template("profil.html", **render_data)
