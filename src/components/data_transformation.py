
from sklearn.feature_extraction.text import TfidfVectorizer
from src.logger import logging
# import pandas as pd

def transform_data(data, features="text"):
    try:
        logging.info("data transformation is started")

        logging.info(data.head())
        logging.info(data.isna().sum())
        # data_new=data.dropna(subset=['subject','email_to'])
        data=data.fillna(value='')
        data.drop_duplicates()
        logging.info(data.isna().sum())

        tfidf = TfidfVectorizer(stop_words='english', max_features=500)
        # combined_features = data[features].apply(lambda x: ' '.join(x), axis=1)
        tfidf_matrix = tfidf.fit_transform(data["text"])
        logging.info("data transformation is completed")
        return tfidf_matrix,tfidf
    except Exception as e:
        logging.info("Error transforming data: {e}")
        return None, None
