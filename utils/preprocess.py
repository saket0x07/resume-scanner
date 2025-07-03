"""
File Name   : preprocess.py
Description : Cleans and tokenizes text using NLTK; removes stopwords and punctuation.
Author      : Saket [github.com/saket0x07]
Date Created: 2025-07-03
Last Updated: 2025-07-03
Version     : 1.0.0

Notes       : Make sure to download NLTK corpora ('punkt', 'stopwords') before running.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Make sure these are downloaded
nltk.download("punkt")
nltk.download("stopwords")

def clean_text(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]

    return tokens
