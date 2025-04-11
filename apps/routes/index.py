from apps.models import *
from flask import render_template, Blueprint

index_route = Blueprint('index_route', __name__)
@index_route.route("/")
def index():
    
    users_query_result = db.session.query(Users)
    
    renderdata = {'users': users_query_result}
    
    return render_template("index.html", **renderdata)
