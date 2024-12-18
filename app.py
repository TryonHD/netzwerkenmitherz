from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template
import json
from database import db_connect
from models import *

app = Flask(__name__)

db_connect(app)

@app.route("/")
def homepage():
    
    users = Users.query.all()
    result = []
    result_keys = []
    
    for usr in users:
        result.append({"id": usr.id,
                       "name": usr.name,
                       "last_name": usr.last_name,
                       "company": usr.company_id.name
                    })
    
    result_keys = list(result[0].keys())
    
    return render_template("index.html", result=(result), key=result_keys)

