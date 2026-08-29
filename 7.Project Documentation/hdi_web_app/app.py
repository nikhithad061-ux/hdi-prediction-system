from flask import Flask, render_template, request
import pickle
import numpy as np
import warnings

app = Flask(__name__)

# Load model
model = pickle.load(open('hdi_model.pkl', 'rb'))

# Classification function
def classify_hdi(hdi):
    if hdi >= 0.8:
        return "Very High"
    elif hdi >= 0.7:
        return "High"
    elif hdi >= 0.55:
        return "Medium"
    else:
        return "Low"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Explicitly extract inputs in exact order: Life Expectancy, Expected Years, Mean Years, GNI
        life = float(request.form.get('life', 0))
        expected = float(request.form.get('expected', 0))
        mean = float(request.form.get('mean', 0))
        gni = float(request.form.get('gni', 0))

        features = np.array([[life, expected, mean, gni]])
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            raw_prediction = float(model.predict(features)[0])
        
        # Clamp HDI prediction to valid range [0.0, 1.0] for gauge and classification
        prediction = min(max(raw_prediction, 0.0), 1.0)
        category = classify_hdi(prediction)
        gauge_percent = prediction * 100.0

        return render_template(
            'index.html',
            prediction=prediction,
            raw_prediction=raw_prediction,
            gauge_percent=gauge_percent,
            category=category,
            prediction_text=f"Predicted HDI: {prediction:.4f} ({category})",
            inputs=request.form
        )
    except Exception as e:
        return render_template(
            'index.html',
            error=f"Error processing calculation: {str(e)}",
            inputs=request.form
        )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
