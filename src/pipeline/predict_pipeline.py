# # src/pipeline/predict_pipeline.py

# import sys
# import pickle
# sys.path.append("..")
# from src.components.data_ingestion import load_data
# from src.components.data_transformation import transform_data

# def run_prediction_pipeline(model_path, tfidf_path, test_data_path):
#     data = load_data(test_data_path)
#     if data is not None:
#         with open(model_path, 'rb') as model_file, open(tfidf_path, 'rb') as tfidf_file:
#             model = pickle.load(model_file)
#             tfidf = pickle.load(tfidf_file)
        
#         X, _ = transform_data(data, features=["text"])
#         if X is not None:
#             predictions = model.predict(X)
#             return predictions
#     return None

# if __name__ == "__main__":
#     model_path = "artifacts/models/support_vector_machine_model.pkl"  # Update this to match the best model saved
#     tfidf_path = "artifacts/models/tfidf.pkl"
#     test_data_path = "artifacts/data/test_data.csv"
#     predictions = run_prediction_pipeline(model_path, tfidf_path, test_data_path)
#     print(predictions)



# predict_message.py
# predict_message.py

import sys
import pickle
import os

sys.path.append("src")
from components.data_transformation import transform_single_message

def load_model(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def predict_message(message, model_path, tfidf_path):
    model = load_model(model_path)
    tfidf = load_model(tfidf_path)

    data = {"message":[message]}
    X = transform_single_message(data, tfidf)
    prediction = model.predict(X)
    
    return prediction[0]

if __name__ == "__main__":
    message = "Re: Jagged Alliance 2 Source Code On 7/4"
    
    model_path = "artifacts/models/support_vector_machine_model.pkl"  # Update this to the best model path
    tfidf_path = "artifacts/models/tfidf.pkl"
    
    prediction = predict_message(message, model_path, tfidf_path)
    print(f"The message is predicted as: {prediction}")
