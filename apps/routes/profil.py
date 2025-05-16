from apps.models import *
from flask import render_template, Blueprint
from .auth import authenticated

profil_route = Blueprint('profil_route', __name__)
@profil_route.route("/profil/")
@authenticated
def profil(user_id):
    
    return render_template("profil.html")