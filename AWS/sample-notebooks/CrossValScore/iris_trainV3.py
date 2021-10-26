from __future__ import print_function

import time
import sys
from io import StringIO
import os
import shutil

import argparse
import csv
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Dictionary to convert labels to indices
LABEL_TO_INDEX = {
    'Iris-virginica': 0,
    'Iris-versicolor': 1,
    'Iris-setosa': 2
}

# Dictionary to convert indices to labels
INDEX_TO_LABEL = {
    0: 'Iris-virginica',
    1: 'Iris-versicolor',
    2: 'Iris-setosa'
}

feature_columns_names = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]
feature_columns_dtype = {
    'sepal_length':'float32',
    'sepal_width':'float32',
    'petal_length':'float32',
    'petal_width':'float32'
}

label_column = 'species'
label_column_dtype = {
    'species':'string'
}
def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def preprocess_data(concat_data):
    
    #map categorical values to numbers
    concat_data['species'] = concat_data['species'].map(LABEL_TO_INDEX)
    
    #fix datatypes
    concat_data['sepal_length']= concat_data['sepal_length'].astype('float32')
    concat_data['sepal_width'] = concat_data['sepal_width'].astype('float32')
    concat_data['petal_length'] = concat_data['petal_length'].astype('float32')
    concat_data['petal_width'] = concat_data['petal_width'].astype('float32')
    concat_data['species'] = concat_data['species'].astype('int')
    
    return concat_data
    
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
                             names=feature_columns_names + [label_column],
                             dtype=merge_two_dicts(feature_columns_dtype, label_column_dtype)) for file in input_files ]
    return raw_data
    
if __name__ == '__main__':
    # Create a parser object to collect the environment variables that are in the
    # default AWS Scikit-learn Docker container.
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    args = parser.parse_args()

    print('\n\n****************************Handling Train Data****************************\n\n')
    
    train_raw_data = read_data_arg(args.train, 'train')
    
    # entire train dataset
    concat_train_data = pd.concat(train_raw_data)
    train_data = preprocess_data(concat_train_data)
    print('\t Preprocessed data:\n')
    print(train_data.head())
    
    # Y column
    train_y = train_data['species']
    
    # X columns
    train_data.drop('species', axis=1, inplace=True)
    

    print(np.shape(train_data), np.shape(train_y))

    
    print("\n\n****************************Training****************************\n\n")
    #Train the LinearRegression model using the fit method
    model = LogisticRegression(max_iter=1000).fit(train_data, train_y)
    
    print('\n\n****************************Handling Test Data****************************\n\n')
    
    test_raw_data = read_data_arg(args.test, 'test')
    
    # entire test dataset
    concat_test_data = pd.concat(test_raw_data)
    test_data = preprocess_data(concat_test_data)
    print('\t Preprocessed data:\n')
    print(test_data.head())
    
    # Y column
    test_y = test_data['species']
    
    # X columns
    test_data.drop('species', axis=1, inplace=True)
    

    print(np.shape(test_data), np.shape(test_y))

    
    print("\n\n****************************Cross Validation****************************\n\n")
    scores = cross_val_score(model, test_data, test_y, cv=5)
    print(scores)

    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

    print("saved model!")


# used to load the model for deployment.
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model

# used to format a request body that is sent to the deployed model.
def input_fn(request_body, content_type):
    print('in input_fun')
    if content_type == 'text/csv':
        print("content_type is text/csv....formatting the request body to a numpy array")
        samples = []
        for r in request_body.split('|'):
            samples.append(list(map(float,r.split(','))))
        return np.array(samples)
    else:
        raise ValueError("This model only supports text/csv input")

# used to make the prediction on the data formatted by the input_fn above using the trained model.
def predict_fn(input_data, model):
    print('in predict_fn')
    predictions = model.predict(input_data)
    print(type(predictions))
    return predictions

# reformats the predictions returned from predict_fn to the final format that will be returned as the API call response.
def output_fn(prediction, content_type):
    print('in output_fn')
    print(prediction)
    return '|'.join([INDEX_TO_LABEL[t] for t in prediction])
