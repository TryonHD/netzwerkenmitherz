from apps.models import *
from run import app
from datetime import datetime
from hashlib import sha256

with app.app_context():

    db.drop_all()
    db.create_all()
    
    Address(street="Dietrichstraße", housenumber="37b", postalcode="33104", city="Paderborn").insert()

    Companys(name="Lenny Industries", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus mollis nulla pellentesque fringilla. Aliquam fermentum felis nec volutpat placerat. Vivamus ultrices pretium ex, eu posuere orci semper auctor. Morbi feugiat congue enim vitae mattis. Integer tristique aliquam risus, et ultricies ligula ultricies eget. Nulla augue ligula, venenatis cursus dapibus vel, ultrices eu sapien. Sed erat urna, malesuada eu hendrerit non, dictum id ipsum. Vestibulum tempus vestibulum justo, quis congue enim bibendum sed.", address_id=1).insert()
    Companys(name="PC2", description="HPC", address_id=1).insert()

    Users(surname="Lenny", name="Korsch", company_id=Companys.query.get(1).id, email="korsch.lenny@gmail.com", password=sha256(b"test1").hexdigest()).insert()
    Users(surname="Sara", name="Piotrowsky", company_id=Companys.query.get(1).id, email="sp@gmail.com", password=sha256(b"test2").hexdigest()).insert()
    Users(surname="Lukas", name="Osterman", company_id=Companys.query.get(2).id, password=sha256(b"test3").hexdigest()).insert()
    Users(surname="Marcel", name="Schwitzkowsky", company_id=Companys.query.get(2).id, password=sha256(b"test4").hexdigest()).insert()


    Events(date=datetime.today().date(), description="War heftig alda!").insert()
    Events(date="2024-03-22", description="War noch viel heftiger!").insert()
    
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.surname=="Lenny").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date=="2024-03-22").one().id, userId=db.session.query(Users).filter(Users.surname=="Lukas").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.surname=="Sara").one().id, attending=True).insert()
    EventAttendees(eventId=db.session.query(Events).filter(Events.date==datetime.today().date()).one().id, userId=db.session.query(Users).filter(Users.surname=="Lukas").one().id, attending=True).insert()

    Roles(name="admin").insert()
    Roles(name="user").insert()

    UserRoles(userId=db.session.query(Users).filter(Users.surname=="Lenny").one().id, roleId=db.session.query(Roles).filter(Roles.name=="admin").one().id).insert()
    UserRoles(userId=db.session.query(Users).filter(Users.surname=="Sara").one().id, roleId=db.session.query(Roles).filter(Roles.name=="user").one().id).insert()