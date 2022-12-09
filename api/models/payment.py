import os
from sqlalchemy.ext.hybrid import hybrid_property
from api import db
from utils.s3_utils import create_presigned_url


class Payment(db.Model):
    __tablename__ = "payments"
    payment_id = db.Column(db.String, primary_key=True)  # stripe generated payment intent id
    dollar_amount = db.Column(db.Float(2), unique=False, nullable=False)
    is_successful = db.Column(db.Boolean, unique=False, nullable=False)
    destination_account_id = db.Column(db.String(50), unique=False, nullable=False)  # generated account id for a school
    user_id = db.Column(db.Integer, unique=False, nullable=True)
    player_id = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self, payment_id, dollar_amount, is_successful, destination_account_id, user_id, player_id):
        self.payment_id = payment_id
        self.dollar_amount = dollar_amount
        self.is_successful = is_successful
        self.destination_account_id = destination_account_id
        self.user_id = user_id
        self.player_id = player_id

    def __repr__(self):
        return f"<Payment {self.payment_id}>"
