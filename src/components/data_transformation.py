
from sklearn.feature_extraction.text import TfidfVectorizer
from logger import logging
import pandas as pd

def transform_data(data, features="text"):
    try:
        logging.info("data transformation is started")
        data=data.fillna(value='')
        data.drop_duplicates()
        tfidf = TfidfVectorizer(stop_words='english', max_features=500)
        tfidf_matrix = tfidf.fit_transform(data["text"])
        logging.info("data transformation is completed")
        return tfidf_matrix,tfidf
    except Exception as e:
        logging.info("Error transforming data: {e}")
        return None, None

# src/components/data_transformation.py

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer

# def transform_data(data, features):
#     tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
#     X = tfidf.fit_transform(data[features[0]] + " " + data[features[1]])
#     return X, tfidf

def transform_single_message(data, tfidf):
    df = pd.DataFrame(data)
    X = tfidf.transform(df['message'])
    return X

