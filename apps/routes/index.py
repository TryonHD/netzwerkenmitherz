from apps.models import *
from flask import render_template, Blueprint, session
from .auth import authenticated

index_route = Blueprint('index_route', __name__)
@index_route.route("/")
@authenticated(["user"])
def index():

    users_query_result = db.session.query(Users)
    
    renderdata = {'users': users_query_result}
    
    return render_template("home.html", **renderdata)