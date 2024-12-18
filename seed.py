from models import *
from app import app
with app.app_context():

    db.drop_all()
    db.create_all()

    Companys(name="Lenny Industries", description="Revolution").insert()
    Companys(name="PC2", description="HPC").insert()

    Users(name="Lenny", last_name="Korsch", company_id=Companys.query.get(1).id).insert()
    Users(name="Sara", last_name="Piotrowsky", company_id=Companys.query.get(1).id).insert()
    Users(name="Lukas", last_name="Osterman", company_id=Companys.query.get(2).id).insert()