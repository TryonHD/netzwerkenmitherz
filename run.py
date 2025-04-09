from flask import Flask
from apps.database import db_connect
from config import *
from apps.routes.index import index_route
from apps.routes.events import events_route
from apps.routes.mitglieder import mitglieder_route
from apps.routes.profil import profil_route
from apps.routes.admin import admin_route

app = Flask(__name__, template_folder=f'{BASE_PATH}apps/templates')

db_connect(app)

app.register_blueprint(index_route)
app.register_blueprint(events_route)
app.register_blueprint(mitglieder_route)
app.register_blueprint(profil_route)
app.register_blueprint(admin_route)
