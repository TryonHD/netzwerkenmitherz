from apps.models import *
from config import *
from flask import render_template, Blueprint, session, url_for
from .auth import authenticated

profil_route = Blueprint('profil_route', __name__)
@profil_route.route("/profil/")
@authenticated(["user"])
def profil():
    
    query_result = db.session.query(Users).filter(Users.id == session["user_id"]).one()
    
    render_data = {"user": query_result,
                   "BASE_PATH": BASE_PATH}
    return render_template("profil.html", **render_data)