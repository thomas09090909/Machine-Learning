# Machine-Learning Heart Disease Prediction Web App

This project is a machine learning web application that predicts the presence of heart disease based on patient health metrics. It includes a trained Random Forest model and a Flask web interface for real-time predictions.

Features

Predicts heart disease using a Random Forest classifier

User-friendly web interface with input form for health metrics

Displays clear results with warning ✅/⚠️ indicators

Handles invalid or missing inputs gracefully

Technologies Used

Python 3.x

Flask – Web framework

Joblib – Model serialization

NumPy – Numerical operations

Scikit-learn – Machine learning model development

HTML/CSS – Frontend form and result display

How It Works

User inputs health features such as age, sex, cholesterol, blood pressure, etc.

Data is sent to the Flask backend.

Backend preprocesses the inputs and predicts using the trained Random Forest model.

Result is displayed on the web page indicating whether heart disease is likely or not.

Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000

Input Features

Age

Sex (0 = female, 1 = male)

Chest pain type (cp)

Resting blood pressure (trestbps)

Cholesterol (chol)

Fasting blood sugar (fbs)

Resting ECG results (restecg)

Maximum heart rate achieved (thalach)

Exercise-induced angina (exang)

ST depression induced by exercise (oldpeak)

Slope of peak exercise ST segment (slope)

Number of major vessels (ca)

Thalassemia (thal)

Example Prediction

✅ No heart disease detected

⚠️ Heart disease likely
