from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and scaler
try:
    model = joblib.load('bhubaneswar_best_model.pkl')
    scaler = joblib.load('bhubaneswar_scaler.pkl')
    print("Model and scaler loaded successfully!")
except:
    print("Warning: Model files not found. Using dummy model.")
    model = None
    scaler = None

# Feature ranges based on Bhubaneswar dataset (you should update these based on your actual data)
FEATURE_RANGES = {
    'CRIME_RATE': {'min': 0.0, 'max': 10.0, 'step': 0.1, 'default': 0.6},
    'GREEN_AREA': {'min': 0.0, 'max': 100.0, 'step': 1.0, 'default': 11.0},
    'INDUSTRIAL_AREA': {'min': 0.0, 'max': 25.0, 'step': 0.5, 'default': 11.0},
    'POLLUTION_LEVEL': {'min': 0.3, 'max': 0.9, 'step': 0.01, 'default': 0.55},
    'AVG_ROOMS': {'min': 3.0, 'max': 9.0, 'step': 0.1, 'default': 6.2},
    'HOUSE_AGE': {'min': 0.0, 'max': 100.0, 'step': 1.0, 'default': 68.0},
    'EMPLOYMENT_DISTANCE': {'min': 1.0, 'max': 12.0, 'step': 0.1, 'default': 3.8},
    'PROPERTY_TAX': {'min': 150, 'max': 500, 'step': 10, 'default': 330},
    'TEACHER_RATIO': {'min': 12.0, 'max': 22.0, 'step': 0.1, 'default': 18.5},
    'MIGRANT_POPULATION': {'min': 0.0, 'max': 400.0, 'step': 1.0, 'default': 356.0},
    'LOW_INCOME_POP': {'min': 1.0, 'max': 40.0, 'step': 0.5, 'default': 12.5}
}

# Categorical options
CATEGORICAL_OPTIONS = {
    'RIVER_PROXIMITY': [
        {'value': 0, 'label': 'Not Near River', 'description': 'Property is not near Kuakhai River'},
        {'value': 1, 'label': 'Near Kuakhai River', 'description': 'Property is near Kuakhai River (Premium Location)'}
    ],
    'LOCALITY_RANK': [
        {'value': 1, 'label': 'Tier 1 - Premium', 'description': 'Premium areas like Nayapalli, Saheed Nagar'},
        {'value': 2, 'label': 'Tier 2 - High', 'description': 'High-end areas like Bapuji Nagar, Ashok Nagar'},
        {'value': 3, 'label': 'Tier 3 - Medium', 'description': 'Medium areas like Patia, Chandrasekharpur'},
        {'value': 4, 'label': 'Tier 4 - Standard', 'description': 'Standard residential areas'},
        {'value': 5, 'label': 'Tier 5 - Basic', 'description': 'Basic residential areas'}
    ]
}

# Famous localities in Bhubaneswar with descriptions
FAMOUS_LOCALITIES = [
    {'name': 'Nayapalli', 'description': 'Premium residential area near government offices'},
    {'name': 'Saheed Nagar', 'description': 'Well-developed residential colony with good amenities'},
    {'name': 'Bapuji Nagar', 'description': 'Central location with shopping facilities'},
    {'name': 'Ashok Nagar', 'description': 'Residential area near Master Canteen'},
    {'name': 'Kharavel Nagar', 'description': 'Commercial and residential hub'},
    {'name': 'Patia', 'description': 'IT hub with modern apartments'},
    {'name': 'Chandrasekharpur', 'description': 'IT corridor with good connectivity'},
    {'name': 'Vani Vihar', 'description': 'Near educational institutions'},
    {'name': 'Rasulgarh', 'description': 'Industrial and residential area'},
    {'name': 'Baramunda', 'description': 'Near bus stand, affordable housing'}
]

@app.route('/')
def home():
    return render_template('index.html', 
                         features=FEATURE_RANGES,
                         categorical=CATEGORICAL_OPTIONS,
                         localities=FAMOUS_LOCALITIES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.get_json()
        
        # Prepare input features in correct order
        feature_values = []
        feature_names = []
        
        # Add numerical features in correct order
        for feature in FEATURE_RANGES.keys():
            value = float(data.get(feature, FEATURE_RANGES[feature]['default']))
            feature_values.append(value)
            feature_names.append(feature)
        
        # Add categorical features
        river_proximity = int(data.get('RIVER_PROXIMITY', 0))
        locality_rank = int(data.get('LOCALITY_RANK', 3))
        
        # Insert categorical features at their correct positions
        # Based on your feature order: RIVER_PROXIMITY is 4th, LOCALITY_RANK is 9th
        feature_values.insert(3, river_proximity)  # After INDUSTRIAL_AREA
        feature_values.insert(8, locality_rank)    # After EMPLOYMENT_DISTANCE
        
        # Convert to numpy array and reshape
        input_array = np.array(feature_values).reshape(1, -1)
        
        # Scale the input
        if scaler:
            scaled_input = scaler.transform(input_array)
        else:
            scaled_input = input_array
        
        # Make prediction
        if model:
            prediction = model.predict(scaled_input)[0]
            # Ensure prediction is not negative
            prediction = max(0, prediction)
        else:
            # Dummy prediction for demo
            prediction = 45.5
        
        # Format response
        response = {
            'success': True,
            'predicted_price': round(prediction, 2),
            'message': f'Estimated House Price: ₹{prediction:.2f} lakhs'
        }
        
    except Exception as e:
        response = {
            'success': False,
            'error': str(e),
            'message': 'Error in prediction. Please check your inputs.'
        }
    
    return jsonify(response)

@app.route('/feature_info')
def feature_info():
    """Provide information about what each feature means"""
    feature_descriptions = {
        'CRIME_RATE': 'Crime rate in the area (per capita). Lower is better.',
        'GREEN_AREA': 'Percentage of green spaces and parks in the area.',
        'INDUSTRIAL_AREA': 'Percentage of land used for industrial purposes. Lower is generally better for residential areas.',
        'RIVER_PROXIMITY': 'Whether the property is near Kuakhai River (premium feature).',
        'POLLUTION_LEVEL': 'Air pollution levels in the area. Lower is better.',
        'AVG_ROOMS': 'Average number of rooms in houses in the area.',
        'HOUSE_AGE': 'Average age of houses in the area (in years).',
        'EMPLOYMENT_DISTANCE': 'Distance to major employment centers (in km).',
        'LOCALITY_RANK': 'Quality rank of the locality (1 being the best).',
        'PROPERTY_TAX': 'Annual property tax rate.',
        'TEACHER_RATIO': 'Student-teacher ratio in local schools. Lower is better.',
        'MIGRANT_POPULATION': 'Percentage of migrant population in the area.',
        'LOW_INCOME_POP': 'Percentage of low-income population in the area.'
    }
    return jsonify(feature_descriptions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5110)