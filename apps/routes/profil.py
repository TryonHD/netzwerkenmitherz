from apps.models import *
from flask import render_template, Blueprint

profil_route = Blueprint('profil_route', __name__)
@profil_route.route("/profil/")
def profil():
    
    return render_template("profil.html")