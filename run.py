from flask import Flask
from apps.database import db_connect
from config import *
from apps.routes.index import index_route

app = Flask(__name__, template_folder=f'{BASE_PATH}apps/templates')

db_connect(app)

app.register_blueprint(index_route)
