from apps.models import *
from flask import render_template, Blueprint

profil_route = Blueprint('profil_route', __name__, url_prefix='/profil')
@profil_route.route("/")
def homepage():
    
    return render_template("profil.html")