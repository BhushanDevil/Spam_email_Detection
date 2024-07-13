# app.py

from flask import Flask, render_template, request
import pickle
import pandas as pd
import os
import sys
# test_numpy.py

import numpy as np

print(np.__version__)
sys.path.append("src")
from src.components.data_transformation import transform_single_message

# Function to load a model from a file
def load_model(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Function to predict spam/ham based on subject and message
def predict_message(message, model_path, tfidf_path):
    model = load_model(model_path)
    tfidf = load_model(tfidf_path)
    
    data = {"message": [message]}
    
    df = pd.DataFrame(data)
    X = tfidf.transform(df['message'])
    prediction = model.predict(X)
    
    return prediction[0]

# Create Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling form submissions
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    
    model_path = "artifacts/models/support_vector_machine_model.pkl"  # Update this to the best model path
    tfidf_path = "artifacts/models/tfidf.pkl"
    
    prediction = predict_message(message, model_path, tfidf_path)
    
    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
