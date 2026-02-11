from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('random_forest_model.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    if request.method == 'POST':
        try:
            # Extract all features from form and convert to float
            features = [
                float(request.form['age']),
                float(request.form['sex']),
                float(request.form['cp']),
                float(request.form['trestbps']),
                float(request.form['chol']),
                float(request.form['fbs']),
                float(request.form['restecg']),
                float(request.form['thalach']),
                float(request.form['exang']),
                float(request.form['oldpeak']),
                float(request.form['slope']),
                float(request.form['ca']),
                float(request.form['thal']),
            ]

            input_array = np.array([features])  # shape (1, 13)

            pred = model.predict(input_array)[0]

            if pred == 1:
                prediction_text = "⚠️ The model predicts presence of heart disease."
            else:
                prediction_text = "✅ The model predicts no heart disease."

        except Exception as e:
            prediction_text = f"Error in prediction: {str(e)}"

    return render_template('index.html', prediction=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
