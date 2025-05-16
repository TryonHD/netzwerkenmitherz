from apps.models import *
from flask import render_template, Blueprint
from .auth import authenticated

mitglieder_route = Blueprint('mitglieder_route', __name__)
@mitglieder_route.route("/mitglieder/")
@authenticated
def mitglieder(user_id):
    
    return render_template("mitglieder.html")