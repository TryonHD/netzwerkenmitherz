from apps.models import *
from flask import render_template, Blueprint

admin_route = Blueprint('admin_route', __name__)
@admin_route.route("/admin/")
def admin():
    
    return render_template("admin.html")