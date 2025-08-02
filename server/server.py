from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Define relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '../model/Bengaluru_House_Data.pickle')
columns_path = os.path.join(BASE_DIR, '../model/columns.json')

# Load model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load data columns
with open(columns_path, 'r') as f:
    data_columns = json.load(f)['data_columns']

location_names = data_columns[3:]  # First 3: total_sqft, bath, bhk

@app.route('/')
def home():
    return "Bangalore House Price Prediction API is running!"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({
        'locations': location_names
    })

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()

    try:
        total_sqft = float(data['total_sqft'])
        bhk = int(data['bhk'])
        bath = int(data['bath'])
        location = data['location']
    except (KeyError, ValueError) as e:
        return jsonify({'error': 'Invalid input format'}), 400

    # Create input vector
    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    try:
        loc_index = data_columns.index(location)
        x[loc_index] = 1
    except ValueError:
        pass  # If location not found, leave it as all 0s

    # Predict
    predicted_price = round(model.predict([x])[0], 2)
    return jsonify({'estimated_price': predicted_price})

if __name__ == "__main__":
    app.run(debug=True)
