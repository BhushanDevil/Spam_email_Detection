# # import sys
# # import os

# # import pandas as pd
# # import numpy as np

# # import dill

# # from src.exception import CustomException

# # def save_object(file_path, obj):
# #     try:
# #         dir_path = os. path. dirname(file_path)
# #         os. makedirs(dir_path, exist_ok=True)
# #         with open(file_path, "w") as file_obj:
# #             dill.dump(obj, file_obj)
# #     except Exception as e:
# #         raise CustomException(e,sys)

# import sys
# import os

# import dill

# from src.exception import CustomException

# # def save_object(file_path, obj):
# #     try:
# #         dir_path = os.path.dirname(file_path)
# #         os.makedirs(dir_path, exist_ok=True)
# #         with open(file_path, "wb") as file_obj:
# #             dill.dump(obj, file_obj)
# #     except Exception as e:
# #         raise CustomException(e, sys)

# import os
# import dill  # Ensure you have dill installed: `pip install dill`
# from src.exception import CustomException
# import sys

# def save_object(file_path, obj):
#     """
#     Save the object to the specified file path using dill for serialization.

#     :param file_path: Path to save the serialized object
#     :param obj: Object to be serialized and saved
#     """
#     try:
#         # Create the directory if it doesn't exist
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)

#         # Save the object using dill
#         with open(file_path, "wb") as file_obj:
#             dill.dump(obj, file_obj)
#     except Exception as e:
#         raise CustomException(e, sys)

# def load_object(file_path):
#     """
#     Load the object from the specified file path using dill for deserialization.

#     :param file_path: Path to load the serialized object from
#     :return: The deserialized object
#     """
#     try:
#         with open(file_path, "rb") as file_obj:
#             return dill.load(file_obj)
#     except Exception as e:
#         raise CustomException(e, sys)


"""updated"""

# src/utils.py

import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
