from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class AccountInfo(db.Model): 
    account_num = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(150))
    total_balance = db.Column(db.Integer)
    #customerInfo_id = db.Column(db.Integer, db.ForeignKey('CustomerInfo.id'))
    



class CustomerInfo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    street_address = db.Column(db.String(500))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    telephone = db.Column(db.String(150))
    birthday = db.Column(db.String(150))
    # foreign key relationship a one to many allows a customer to have multiple bank accounts
    #account_info = db.relationship('AccountInfo')




