from database import db

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(100), 
                     nullable=False)
    
    last_name = db.Column(db.String(100),
                         nullable=False)
    
    company = db.Column(db.String(255),
                       db.ForeignKey('company.id'),
                       nullable=False)

class Company(db.Model):
    
    __tablename__ = 'company'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(100), 
                     nullable=False)
    
    description = db.Column(db.String(5000), 
                            nullable=False)