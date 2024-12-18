from database import db

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
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    
    company = db.relationship('Companys', backref='user')


class Companys(BaseModel):
    
    __tablename__ = 'company'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(5000), nullable=True)
