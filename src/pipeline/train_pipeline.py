"""updated"""
# src/pipeline/train_pipeline.py

import sys
import os
import pickle

sys.path.append("..")
from src.components.data_ingestion import load_data
from src.components.data_transformation import transform_data
from src.components.model_trainer import train_and_evaluate_models, get_models
from src.logger import logging
from src.data_preprocess import data_preprocessing


def save_model(model, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

def run_training_pipeline(train_data_path):
    data = load_data(train_data_path)
    logging.info("Loaded data")

    if data is not None:
        try:
            X,tfidf= transform_data(data, features="text")

            if X is not None:
                results, models = train_and_evaluate_models(X, data['label'])
                best_model_name = max(results, key=lambda x: results[x]['F1 Score'])
                best_model = models[best_model_name]
                os.makedirs("artifacts/models", exist_ok=True)
                save_model(best_model, f"artifacts/models/{best_model_name.replace(' ', '_').lower()}_model.pkl")
                save_model(tfidf, "artifacts/models/tfidf.pkl")
                for model_name, metrics in results.items():
                    logging.info(f"Model: {model_name}")
                    for metric_name, value in metrics.items():
                        print(f"{metric_name}: {value}")
                    logging.info("-" * 30)
                return results
            return None
        except Exception as e:
            logging.info(f"Error train_pipeline: {e}")
            return None, None

if __name__ == "__main__":
    data_preprocessing()
    train_data_path = "artifacts/train.csv"
    run_training_pipeline(train_data_path)


