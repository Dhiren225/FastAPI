from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
import datetime

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define Customers class inheriting from Base

class Customers(Base):
 
    __tablename__ = 'customer_test_tab'

    ID=db.Column(db.Integer,primary_key=True)
    
    FIRST_NAME = db.Column(db.String,
                           primary_key=False)
    LAST_NAME = db.Column(db.String(50),
                          primary_key=False)
    EMAIL = db.Column(db.String(50),
                       primary_key=False)

    CUSTOMER_TYPE = db.Column(db.String(50),
                       primary_key=False)
    
    CREATED_ON = db.Column(db.DateTime)
