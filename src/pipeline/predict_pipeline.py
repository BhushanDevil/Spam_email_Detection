# src/pipeline/predict_pipeline.py

import sys
import pickle
sys.path.append("..")
from components.data_ingestion import load_data
from components.data_transformation import transform_data

def run_prediction_pipeline(model_path, tfidf_path, test_data_path):
    data = load_data(test_data_path)
    if data is not None:
        with open(model_path, 'rb') as model_file, open(tfidf_path, 'rb') as tfidf_file:
            model = pickle.load(model_file)
            tfidf = pickle.load(tfidf_file)
        
        X, _ = transform_data(data, features=["text"])
        if X is not None:
            predictions = model.predict(X)
            return predictions
    return None

if __name__ == "__main__":
    model_path = "artifacts/models/random_forest_model.pkl"  # Update this to match the best model saved
    tfidf_path = "artifacts/models/tfidf.pkl"
    test_data_path = "artifacts/data/test_data.csv"
    predictions = run_prediction_pipeline(model_path, tfidf_path, test_data_path)
    print(predictions)
