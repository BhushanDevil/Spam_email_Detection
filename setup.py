# from setuptools import find_packages, setup
# from typing import List
# from src.logger import logging

# logging.info("setup. py has been started")

# HYPEN_E_DOT = '-e .'

# def get_requirements(file_path: str) -> List[str]:
#     '''This function will return a list of requirements.'''
#     requirements = []
#     with open(file_path, 'r', encoding='utf-8') as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.strip() for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements

# setup(
#     name='Spam Detection',
#     version='0.0.1',
#     author='Bhushan Ankush Vanjiwale',
#     author_email='rusivanjare7@gmail.com',
#     description='A package for spam detection',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt'),
# )

"""updated"""
# setup.py

from setuptools import setup, find_packages

setup(
    name="Spam_Email_Detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "numpy",
        # Add any other dependencies required for your project
    ],
)

