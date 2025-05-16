from apps.database import db

class BaseModel(db.Model):
    __abstract__ = True  # Prevents this class from being treated as a table

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e  # Re-raise the exception for further handling
        finally:
            db.session.close()

class Users(BaseModel):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phonenumber = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(255), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('companys.id'), nullable=True)
    
    company = db.relationship('Companys', backref='user')

class Companys(BaseModel):
    
    __tablename__ = 'companys'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=True)
    domain = db.Column(db.String(200), nullable=True)
    
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    
    address = db.relationship('Address', backref='company')
  
class Events(BaseModel):
    
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(5000), nullable=True)
    location = db.Column(db.String(200), nullable=True)

class EventAttendees(BaseModel):
    
    __tablename__ = 'event_attendees'
    
    eventId = db.Column(db.Integer, db.ForeignKey('events.id'), primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    
    attending = db.Column(db.Boolean, nullable=False)
    attendance = db.Column(db.Boolean)

    event = db.relationship('Events', backref='event_attendance')
    user = db.relationship('Users', backref='event_attendance')

class Address(BaseModel):
    
    __tablename__ = 'address'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.String(10), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(100), nullable=False)

class Professions(BaseModel):
    
    __tablename__ = 'professions'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)

class CompanyProfessions(BaseModel):
    
    __tablename__ = 'company_professions'
    
    companyId = db.Column(db.Integer, db.ForeignKey('companys.id'), primary_key=True, nullable=False)
    professionId = db.Column(db.Integer, db.ForeignKey('professions.id'), primary_key=True, nullable=False)

    company = db.relationship('Companys', backref='company_professions')
    profession = db.relationship('Professions', backref='company_professions')

class Roles(BaseModel):

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    

class UserRoles(BaseModel):

    __tablename__ = "user_roles"

    userId = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True, nullable=False)

    role = db.relationship('Roles', backref='user_roles')
    user = db.relationship('Users', backref='user_roles')