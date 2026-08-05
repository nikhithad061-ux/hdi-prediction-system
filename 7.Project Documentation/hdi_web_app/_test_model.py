import pickle
import numpy as np
import sys

with open('_test_output.log', 'w') as f:
    sys.stdout = f
    sys.stderr = f
    
    try:
        print("Loading model...")
        model = pickle.load(open('hdi_model.pkl', 'rb'))
        print("Model loaded successfully!")
        
        # Inputs: life, expected, mean, gni
        features = [72.5, 12.8, 8.4, 15400]
        final_features = [np.array(features)]
        print("Features:", final_features)
        prediction = model.predict(final_features)[0]
        print(f"Prediction: {prediction}")
    except Exception as e:
        import traceback
        traceback.print_exc()
