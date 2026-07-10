from flask import Flask, render_template, request
import pickle
import numpy as np

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
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)[0]
    category = classify_hdi(prediction)

    return render_template(
        'index.html',
        prediction_text=f"Predicted HDI: {prediction:.4f} ({category})"
    )

if __name__ == "__main__":
    app.run(debug=True)