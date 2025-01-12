from apps.models import *
from run import app
from datetime import datetime

with app.app_context():

    db.drop_all()
    db.create_all()

    Companys(name="Lenny Industries", description="Revolution").insert()
    Companys(name="PC2", description="HPC").insert()

    Users(name="Lenny", last_name="Korsch", company_id=Companys.query.get(1).id).insert()
    Users(name="Sara", last_name="Piotrowsky", company_id=Companys.query.get(1).id).insert()
    Users(name="Lukas", last_name="Osterman", company_id=Companys.query.get(2).id).insert()
    
    Events(date=datetime.today().date(), description="War heftig alda!").insert()
    Events(date="2024-03-22", description="War noch viel heftiger!").insert()
    
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.name=="Lenny").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.name=="Lukas").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.name=="Sara").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.name=="Lukas").one().id, attending=True).insert()
