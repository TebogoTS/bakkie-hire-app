from models import Pricing, db

def calculate_price(distance, weight, vehicle_type):
    pricing = Pricing.query.filter_by(vehicle_type=vehicle_type).first()

    if not pricing:
        return None
    
    price = pricing.base_price
    price += distance * pricing.price_per_km

    return price