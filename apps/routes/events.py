from apps.models import *
from flask import render_template, Blueprint, session
from sqlalchemy import desc
from .auth import authenticated
import datetime

events_route = Blueprint("events_route", __name__)


@events_route.route("/events/")
@authenticated(["admin"])
def events():
    events_query_result = db.session.query(Events).order_by(desc(Events.date)).all()

    # events = []

    # for ev in events_query_result:
    #    events.append({
    #        "id": ev.id,
    #        "date": ev.date,
    #        "desc": ev.description
    #        })

    today = datetime.datetime.today()
    future_events = []
    past_events = []

    for event in events_query_result:
        if event.date >= today:
            future_events.append(event)
        else:
            past_events.append(event)

    renderdata = {
        "future_events": future_events,
        "past_events": past_events,
        "current_user": db.session.query(Users)
        .filter(Users.id == session["user_id"])
        .one(),
    }

    # return render_template("events.html", foo=bar)
    return render_template("events.html", **renderdata)
