from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, String, DECIMAL, Integer


db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    price = Column(DECIMAL)


'''
     SUCCESFUL MIGRATIONS
     INFO/nINFO/nINFO

      DB ERRORS
many lines of errors starting with file:check imports,syntax errors 
error with info/DDL and target dtabase>>check history then proceed to upgrade
error starting with usage:....or could not import app>>wrong directory
'''