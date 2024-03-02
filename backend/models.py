from config import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'<User {self.email}>'
    
class Pricing(db.Model):
    __tablename__ = 'pricing'

    pricing_id = db.Column(db.Integer, primary_key=True)
    base_price = db.Column(db.Numeric(10, 2), nullable=False)
    price_per_km = db.Column(db.Numeric(10, 2), nullable=False)
    vehicle_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pricing {self.vehicle_type}'