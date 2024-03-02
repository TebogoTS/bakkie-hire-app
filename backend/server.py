from flask import Flask
from config import db
import os
from api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakkiehire.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if not os.path.exists('bakkiehire.db'):
    with app.app_context():
        db.create_all()

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)