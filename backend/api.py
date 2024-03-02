from flask import request, jsonify, Blueprint
from services.pricing import calculate_price
from models import db, User
from . import api

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(email=data['email'], name=data['name'], phone_number=data['phone_number'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@api.route('/calculate-price', methods=['POST'])
def get_estimated_price():
    data = request.json
    estimated_price = calculate_price(data['distance'], data['weight'], data['vehicle'])

    if estimated_price is None:
        return jsonify({'message': 'Pricing information not available for the selected vehicle type'}), 404
    
    return jsonify({'estimated_price': estimated_price}), 200