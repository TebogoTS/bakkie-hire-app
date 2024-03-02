from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route('/api/ping', methods=['GET'])
def ping():
    """Endpoint to check if the server is running"""
    return jsonify({'message': 'pong'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)