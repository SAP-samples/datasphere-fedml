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

from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import Binarizer, StandardScaler, OneHotEncoder

from sklearn.linear_model import LinearRegression

# https://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/
# Since we get a headerless CSV file we specify the column names here.
feature_columns_names = [
    'Units_Sold', 'Unit_Price', 'Unit_Cost',
       'Total_Revenue', 'Total_Cost']

label_column = 'Total_Profit'

feature_columns_dtype = {
    'Units_Sold': "int64",
    'Unit_Price': "float64",
    'Unit_Cost': "float64",
    'Total_Revenue': "float64",
    'Total_Cost': "float64"}

label_column_dtype = {'Total_Profit': "float64"} # +1.5 gives the age in years

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))

    raw_data = [ pd.read_csv(file, 
                             header=None, 
                             names=feature_columns_names + [label_column],
                             dtype=merge_two_dicts(feature_columns_dtype, label_column_dtype)) for file in input_files ]
    concat_data = pd.concat(raw_data)
    y = concat_data[label_column]

    concat_data.drop(label_column, axis=1, inplace=True)
    
    print(np.shape(concat_data), np.shape(y))
    
    X_train, X_test, y_train, y_test = train_test_split(concat_data, y, test_size=0.3)
    
    print('\n\n****************************X_train and X_test****************************\n\n')
    print(X_train)
    print('\n\n')
    print(X_test)
    
    print('\n\n****************************y_train and y_test****************************\n\n')
    print(y_train)
    print('\n\n')
    print(y_test)
    
    #Train the LinearRegression model using the fit method
    model = LinearRegression().fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    
    print('\n\n\nScore for fit: ' + str(score) + '\n\n')

    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

    print("saved model!")


def input_fn(input_data, content_type):
    """Parse input data payload

    We currently only take csv input. Since we need to process both labelled
    and unlabelled data we first determine whether the label column is present
    by looking at how many columns were provided.
    """
    if content_type == 'text/csv':
        print('Processing Input Data...')
        # Read the raw input data as CSV.
        df = pd.read_csv(StringIO(input_data), 
                         header=None)

        if len(df.columns) == len(feature_columns_names) + 1:
            # This is a labelled example, includes the ring label
            df.columns = feature_columns_names + [label_column]
        elif len(df.columns) == len(feature_columns_names):
            # This is an unlabelled example.
            df.columns = feature_columns_names
        print('Data loaded')
        return df
    else:
        raise ValueError("{} not supported by script!".format(content_type))


def model_fn(model_dir):
    """Deserialize fitted model
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf