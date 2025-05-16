from apps.models import *
from flask import render_template, Blueprint
from sqlalchemy import desc
from .auth import authenticated

events_route = Blueprint('events_route', __name__)
@events_route.route("/events/")
@authenticated(["admin"])
def events():
    
    events_query_result = db.session.query(Events).order_by(desc(Events.date)).all() 
    
    # events = []
    
    #for ev in events_query_result:
    #    events.append({
    #        "id": ev.id,
    #        "date": ev.date,
    #        "desc": ev.description
    #        })

    renderdata = {'events': events_query_result}
    
    # return render_template("events.html", foo=bar)
    return render_template("events.html", **renderdata)
