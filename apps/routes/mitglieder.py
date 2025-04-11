from apps.models import *
from flask import render_template, Blueprint

mitglieder_route = Blueprint('mitglieder_route', __name__)
@mitglieder_route.route("/mitglieder/")
def mitglieder():
    
    return render_template("mitglieder.html")