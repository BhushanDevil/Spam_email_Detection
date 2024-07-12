# run_all.py

import os
import subprocess
import sys

from src.logger import logging


logging.info ("Spam email detection is Started")
def install_dependencies():
    try:
        logging.info("installing Library Dependencies from requirements is started")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        logging.info(f"Error installing dependencies: {e}")
        sys.exit(1)

def run_training_pipeline():
    try:
        logging.info("train pipeline is started")
        subprocess.check_call([sys.executable, "src/pipeline/train_pipeline.py"])
    except subprocess.CalledProcessError as e:
        logging.info(f"Error running training pipeline: {e}")
        sys.exit(1)

def run_prediction_pipeline():
    try:
        logging.info("prediction pipleine is started")
        subprocess.check_call([sys.executable, "src/pipeline/predict_pipeline.py"])
    except subprocess.CalledProcessError as e:
        logging.info(f"Error running prediction pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    logging.info("Installing dependencies...")
    install_dependencies()
    
    logging.info("Running training pipeline...")
    run_training_pipeline()

    # Uncomment the following lines if you want to run the prediction pipeline automatically after training
    # print("Running prediction pipeline...")
    # run_prediction_pipeline()

    print("All steps completed successfully.")
