from apps.models import *
from run import app
from datetime import datetime

with app.app_context():

    db.drop_all()
    db.create_all()
    
    Address(street="Dietrichstraße", house_number="37b", postal_code="33104", city="Paderborn").insert()

    Companys(name="Lenny Industries", description="Revolution", address_id=1).insert()
    Companys(name="PC2", description="HPC", address_id=1).insert()

    Users(surname="Lenny", name="Korsch", company_id=Companys.query.get(1).id, email="korsch.lenny@gmail.com").insert()
    Users(surname="Sara", name="Piotrowsky", company_id=Companys.query.get(1).id).insert()
    Users(surname="Lukas", name="Osterman", company_id=Companys.query.get(2).id).insert()
    Users(surname="Marcel", name="Schwitzkowsky", company_id=Companys.query.get(2).id).insert()


    Events(date=datetime.today().date(), description="War heftig alda!").insert()
    Events(date="2024-03-22", description="War noch viel heftiger!").insert()
    
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.surname=="Lenny").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.surname=="Lukas").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.surname=="Sara").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.surname=="Lukas").one().id, attending=True).insert()