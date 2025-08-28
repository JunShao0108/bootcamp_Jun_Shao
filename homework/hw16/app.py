from flask import Flask, jsonify, request
import joblib
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import threading
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MODEL_DIR = os.getenv('MODEL_DIR', '/Users/junshao/bootcamp_Jun_Shao/homework/hw13/model')  # Default path

app = Flask(__name__)

# Load pickled model once at startup
try:
    model = joblib.load(os.path.join(MODEL_DIR, 'linear_model.pkl'))
    print(f"Model loaded with {model.n_features_in_} features")
except FileNotFoundError:
    print(f"Error: Model file not found at {os.path.join(MODEL_DIR, 'linear_model.pkl')}")
    exit(1)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    exit(1)

# Validate model features
n_features = model.n_features_in_
print(f"Expected number of features: {n_features}")

@app.route('/predict', methods=['POST'])
def predict():
    """
    POST /predict with JSON features.
    Returns a predicted SalePrice based on input features.
    
    Request JSON: {'features': [float, ...]} (length must match model.n_features_in_)
    Response: {'prediction': float} or {'error': str, 'status': int}
    """
    try:
        data = request.get_json(force=True)
        features = data.get('features')
        if features is None:
            return jsonify({'error': 'No features provided', 'status': 400}), 400
        if not isinstance(features, list) or len(features) != n_features:
            return jsonify({'error': f'Invalid feature array length, expected {n_features}', 'status': 400}), 400
        features = np.array(features, dtype=float).reshape(1, -1)
        pred = model.predict(features)[0]
        return jsonify({'prediction': float(pred)})
    except ValueError as e:
        return jsonify({'error': f'Invalid feature values: {str(e)}', 'status': 400}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}', 'status': 500}), 500

@app.route('/predict/<float:input1>', methods=['GET'])
def predict_one(input1):
    """
    GET /predict/<input1> for single feature input.
    Pads remaining features with zeros for prediction.
    
    Args:
        input1 (float): First feature value.
    Response: {'prediction': float} or {'error': str, 'status': int}
    """
    try:
        features = np.array([input1] + [0.0] * (n_features - 1), dtype=float).reshape(1, -1)
        pred = model.predict(features)[0]
        return jsonify({'prediction': float(pred)})
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}', 'status': 500}), 500

@app.route('/predict/<float:input1>/<float:input2>', methods=['GET'])
def predict_two(input1, input2):
    """
    GET /predict/<input1>/<input2> for two features.
    Pads remaining features with zeros for prediction.
    
    Args:
        input1 (float): First feature value.
        input2 (float): Second feature value.
    Response: {'prediction': float} or {'error': str, 'status': int}
    """
    try:
        features = np.array([input1, input2] + [0.0] * (n_features - 2), dtype=float).reshape(1, -1)
        pred = model.predict(features)[0]
        return jsonify({'prediction': float(pred)})
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}', 'status': 500}), 500

@app.route('/plot')
def plot():
    """
    GET /plot to return a simple chart.
    Displays a sample R² trend based on model performance.
    
    Response: HTML with embedded PNG image.
    """
    try:
        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0.68, 0.714, 0.712])
        ax.set_title('Sample R² Trend')
        ax.set_xlabel('Scenario')
        ax.set_ylabel('R²')
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img_bytes = base64.b64encode(buf.read()).decode('utf-8')
        return f'<img src="data:image/png;base64,{img_bytes}"/>'
    except Exception as e:
        return jsonify({'error': f'Plot generation failed: {str(e)}', 'status': 500}), 500

def run_flask():
    """
    Run the Flask application on port 5000.
    """
    app.run(port=5001, debug=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
