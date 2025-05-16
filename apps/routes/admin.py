from apps.models import *
from flask import render_template, Blueprint
from .auth import authenticated

admin_route = Blueprint('admin_route', __name__)
@admin_route.route("/admin/")
@authenticated
def admin(user_idw):
    
    return render_template("admin.html")