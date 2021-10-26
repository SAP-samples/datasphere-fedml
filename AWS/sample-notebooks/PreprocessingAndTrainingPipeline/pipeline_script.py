import argparse
import csv
import json
import joblib
import os

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from time import time
import sklearn

# https://www.kaggle.com/mantri7/imdb-movie-reviews-dataset?select=train_data+%281%29.csv
############################## Global variables ##############################



column_names = ['0', '1']

############################## Helper Functions ##############################
def read_data_arg(argument, channel):
    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(argument, file) for file in os.listdir(argument) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(argument, channel))

    raw_data = [ pd.read_csv(file, 
                             header=None, 
                             names=column_names ) for file in input_files ]
    
    data = pd.concat(raw_data)
    return data
    
############################## Required Functions ##############################
def model_fn(model_dir):
    """Deserialize fitted model"""
    print('storing the model....')
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

def input_fn(request_body,content_type):
    print('in input_fun')
    if content_type == 'application/json':
        print("content_type is application/json....formatting the request body to a dataframe")
        data = json.loads(request_body)
        data = pd.Series(data)
        return data
    else:
        raise ValueError("This model only supports application/json input")
    
def predict_fn(input_data, model):
    print('in predict_fn')
    result = model.predict(input_data)
    print(type(result))
    return result

    
############################## Training Script Part ##############################
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    
    args = parser.parse_args()
    print('The scikit-learn version is {}.'.format(sklearn.__version__))

    print('\n\n********* Handling Data *********\n\n')
    train = read_data_arg(args.train, 'train')
    train = train.head(30000)
    print("training data\n")
    print(train)
    
    train_X = train['0']   # '0' corresponds to Texts/Reviews
    train_y = train['1']   # '1' corresponds to Label (1 - positive and 0 - negative)
    print(train_X)
    print(train_y)

    t = time()
    vectorizer = TfidfVectorizer()
    naive_bayes_classifier = MultinomialNB()

    pipeline = Pipeline([('vectorizer', vectorizer), ('naiveBayes', naive_bayes_classifier)])
    pipeline.fit(train_X, train_y)
    duration = time() - t
    print("train time:  %0.3fs" % duration)

    print('storing model....')
    
    joblib.dump(pipeline, os.path.join(args.model_dir, "model.joblib"))

    print("saved model!")



