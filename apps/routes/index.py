from apps.models import *
from flask import render_template, Blueprint

index_route = Blueprint('index_route', __name__, url_prefix='/')
@index_route.route("/")
def homepage():
    
    users_query_result = db.session.query(Users)
    
    renderdata = {'users': users_query_result}
    
    return render_template("index.html", **renderdata)
