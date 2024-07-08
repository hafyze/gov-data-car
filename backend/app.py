# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/carmakers', methods=['GET'])
def get_carmakers():
    # Dummy data for example
    carmakers_data = [
        {"id": 1, "name": "Toyota"},
        {"id": 2, "name": "Honda"},
        {"id": 3, "name": "Proton"}
    ]
    return jsonify(carmakers_data)

if __name__ == '__main__':
    app.run(debug=True)
