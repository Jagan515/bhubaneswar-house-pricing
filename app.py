import joblib
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load pipeline (scaler + model together)
pipeline = joblib.load("lr_pipeline.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data']

        # Ensure same feature order
        feature_order = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 
                         'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

        input_values = [data[key] for key in feature_order]
        final_input = np.array(input_values).reshape(1, -1)

        # Pipeline already handles scaling + prediction
        output = pipeline.predict(final_input)

        return jsonify(float(output[0]))

    except KeyError as e:
        return jsonify({"error": f"Missing key in JSON data: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
