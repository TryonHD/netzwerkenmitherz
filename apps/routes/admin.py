from apps.models import *
from flask import render_template, Blueprint

admin_route = Blueprint('admin_route', __name__, url_prefix='/admin')
@admin_route.route("/")
def homepage():
    
    return render_template("admin.html")