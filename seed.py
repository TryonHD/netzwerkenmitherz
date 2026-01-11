from apps.models import *
from run import app
import datetime
from hashlib import sha256

today = datetime.datetime.today().replace(hour=19, minute=0, second=0, microsecond=0)
tomorrow = (today + datetime.timedelta(days=1)).replace(
    hour=18, minute=30, second=0, microsecond=0
)
yesterday = (today - datetime.timedelta(days=1)).replace(
    hour=18, minute=0, second=0, microsecond=0
)

with app.app_context():
    db.drop_all()
    db.create_all()

    Professions(name="Tischler").insert()
    Professions(name="Metaller").insert()
    Professions(name="Dachtecker").insert()
    Professions(name="Elektriker").insert()
    Professions(name="Schreiner").insert()
    Professions(name="Maurer").insert()

    Companys(
        name="Lenny Industries",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus mollis nulla pellentesque fringilla. Aliquam fermentum felis nec volutpat placerat. Vivamus ultrices pretium ex, eu posuere orci semper auctor. Morbi feugiat congue enim vitae mattis. Integer tristique aliquam risus, et ultricies ligula ultricies eget. Nulla augue ligula, venenatis cursus dapibus vel, ultrices eu sapien. Sed erat urna, malesuada eu hendrerit non, dictum id ipsum. Vestibulum tempus vestibulum justo, quis congue enim bibendum sed.",
        street="Dietrichstraße",
        housenumber="37b",
        postalcode="33104",
        city="Paderborn",
    ).insert()

    Companys(
        name="PC2",
        description="HPC",
        street="Dietrichstraße",
        housenumber="37b",
        postalcode="33104",
        city="Paderborn",
    ).insert()

    CompanyProfessions(companyId=1, professionId=1).insert()
    CompanyProfessions(companyId=1, professionId=2).insert()
    CompanyProfessions(companyId=1, professionId=3).insert()
    CompanyProfessions(companyId=1, professionId=4).insert()
    CompanyProfessions(companyId=1, professionId=5).insert()
    CompanyProfessions(companyId=1, professionId=6).insert()

    Users(
        surname="Lenny",
        name="Korsch",
        company_id=Companys.query.get(1).id,
        email="korsch.lenny@gmail.com",
        password=sha256(b"test1").hexdigest(),
    ).insert()

    Users(
        surname="Sara",
        name="Piotrowsky",
        company_id=Companys.query.get(1).id,
        email="sp@gmail.com",
        password=sha256(b"test2").hexdigest(),
    ).insert()

    Users(
        surname="Lukas",
        name="Osterman",
        company_id=Companys.query.get(2).id,
        password=sha256(b"test3").hexdigest(),
    ).insert()

    Users(
        surname="Marcel",
        name="Schwitzkowsky",
        company_id=Companys.query.get(2).id,
        password=sha256(b"test4").hexdigest(),
    ).insert()

    Users(
        surname="Fred",
        name="Ned",
        company_id=Companys.query.get(2).id,
        password=sha256(b"test4").hexdigest(),
    ).insert()

    Users(
        surname="Liam",
        name="Schwum",
        company_id=Companys.query.get(2).id,
        password=sha256(b"test4").hexdigest(),
    ).insert()

    Events(date=today, description="War heftig alda!").insert()
    Events(date=tomorrow, description="War noch viel heftiger!").insert()
    Events(date=yesterday, description="War nooooooch heftiger!").insert()
    print("Test")
    print(yesterday)
    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == yesterday).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Lenny").one().id,
        attendance=True,
    ).insert()

    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == yesterday).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Lukas").one().id,
        attendance=False,
    ).insert()

    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == today).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Sara").one().id,
        attendance=True,
    ).insert()

    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == today).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Lukas").one().id,
        attendance=False,
    ).insert()

    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == tomorrow).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Sara").one().id,
        attendance=True,
    ).insert()

    EventAttendees(
        eventId=db.session.query(Events).filter(Events.date == tomorrow).one().id,
        userId=db.session.query(Users).filter(Users.surname == "Lukas").one().id,
        attendance=False,
    ).insert()

    Roles(name="admin").insert()

    Roles(name="user").insert()

    UserRoles(
        userId=db.session.query(Users).filter(Users.surname == "Lenny").one().id,
        roleId=db.session.query(Roles).filter(Roles.name == "admin").one().id,
    ).insert()

    UserRoles(
        userId=db.session.query(Users).filter(Users.surname == "Sara").one().id,
        roleId=db.session.query(Roles).filter(Roles.name == "user").one().id,
    ).insert()
