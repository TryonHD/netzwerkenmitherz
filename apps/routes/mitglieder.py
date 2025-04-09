from apps.models import *
from flask import render_template, Blueprint

mitglieder_route = Blueprint('mitglieder_route', __name__, url_prefix='/mitglieder')
@mitglieder_route.route("/")
def homepage():
    
    return render_template("mitglieder.html")