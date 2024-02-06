from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class UserRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    request_count = db.Column(db.Integer, default=0, nullable=False)
    last_request_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"UserRequest('{self.ip_address}', '{self.request_count}')"
