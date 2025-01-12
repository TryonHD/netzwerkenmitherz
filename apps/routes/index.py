from apps.models import *
from flask import render_template, Blueprint

index_route = Blueprint('index_route', __name__, url_prefix='/index')
@index_route.route("/")
def homepage():
    
    users = Users.query.all()
    result = []
    result_keys = []
    
    for usr in users:
        result.append({
                    "id": usr.id,
                    "name": usr.name,
                    "last_name": usr.last_name,
                    "company": usr.company.name,
                    "comp_desc": usr.company.description
                    })
    
    result_keys = list(result[0].keys())
    
    return render_template("index.html", result=(result), keys=result_keys)
