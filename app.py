from flask import Flask, render_template, request
import pickle
import numpy as np

# ✅ Load trained model and preprocessor
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    try:
        # ✅ Collect form inputs
        Year = int(request.form['Year'])
        AverageRainfall = float(request.form['AverageRainfall'])
        Pesticide = float(request.form['Pesticide'])
        AverageTemp = float(request.form['AverageTemp'])
        Area = request.form['Area']
        Item = request.form['Item']

        # ✅ Prepare data for model
        features = np.array([[Year, AverageRainfall, Pesticide, AverageTemp, Area, Item]], dtype=object)
        transformed_features = preprocessor.transform(features)

        # ✅ Make prediction
        prediction = dtr.predict(transformed_features)[0]

        # ✅ Return result to frontend
        return render_template('index.html', prediction_text=f"🌾 Predicted Crop Yield: {prediction:.1f} hg/ha")

    except Exception as e:
        # Show error on page
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
