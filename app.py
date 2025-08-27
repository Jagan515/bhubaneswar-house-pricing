import joblib
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load pipeline (scaler + model together)
pipeline = joblib.load("lr_pipeline.pkl")

# Ensure same feature order (used in both API + HTML form)
feature_order = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        input_values = [data[key] for key in feature_order]
        final_input = np.array(input_values).reshape(1, -1)
        output = pipeline.predict(final_input)
        return jsonify(float(output[0]))
    except KeyError as e:
        return jsonify({"error": f"Missing key in JSON data: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values from HTML form in same order as feature_order
        data = [float(x) for x in request.form.values()]
        final_input = np.array(data).reshape(1, -1)
        output = pipeline.predict(final_input)
        return render_template("home.html", prediction_text=f"The predicted price is {output[0]:.2f}")
    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
