import os
import logging

from hdbcli import dbapi

import pandas as pd
import numpy as np

from sklearn import model_selection
import joblib
# from tensorflow import gfile
import pickle
from trainer import metadata
from google.cloud import storage
from fedml_gcp import DbConnection
from sklearn.model_selection import train_test_split

    
def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    logging.info(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def dump_model(bucket_name, object_to_dump, output_path):
    """Pickle the object and save to the output_path.
    Args:
      object_to_dump: Python object to be pickled
      output_path: (string) output path which can be Google Cloud Storage
    Returns:
      None
    """
#     with open(output_path, 'wb') as model_file:
#           pickle.dump(object_to_dump, model_file)
#     if not gfile.Exists(output_path):
#         gfile.MakeDirs(os.path.dirname(output_path))
#     with gfile.Open(output_path, 'w') as wf:
#         joblib.dump(object_to_dump, wf)
        
    with open('model.pkl', 'wb') as model_file:
      pickle.dump(object_to_dump, model_file)
    
    upload_blob(bucket_name, 'model.pkl', output_path+'model.pkl')
    

def get_dwc_data(table, size):
    columns_dtype = {
        'sepal_length':'float32',
        'sepal_width':'float32',
        'petal_length':'float32',
        'petal_width':'float32',
        'species':'string'}
    
    db = DbConnection(package_name='trainer')
    res, column_headers = db.get_data_with_headers(table_name=table, size=size)
    data = pd.DataFrame(res, columns=column_headers)
    data = data.sample(frac=1).reset_index(drop=True)
    return data.astype(columns_dtype).head(100)
    
def handle_data(model_data):

    X_train, X_test, y_train, y_test = train_test_split(model_data.drop(['species'], axis=1), model_data['species'], test_size=0.3)
    
    train_data = pd.concat([X_train, y_train], axis=1)
    logging.info('\n******** Train Data ********\n')
    logging.info(train_data.head())

    test_data = pd.concat([X_test, y_test], axis=1)
    logging.info('\n******** Test Data ********\n')
    logging.info(test_data.head())
    
    # preprocess train data - convert categorical to numerical
    train_data = preprocess_data(train_data)
    logging.info('\n******** Preprocessed Train data:********\n')
    logging.info(train_data.head())

    # preprocess test data - convert categorical to numerical
    test_data = preprocess_data(test_data)
    logging.info('\n******** Preprocessed Test data:********\n')
    logging.info(test_data.head())
    
    #TRAIN dataset
    train_y = train_data['species']
    train_data.drop(['species'], axis=1, inplace=True)

    #TEST dataset
    test_y = test_data['species']

    # test X columns
    test_data.drop(['species'], axis=1, inplace=True)

    logging.info("Train data shape " + str(np.shape(train_data)) + str(np.shape(train_y)))
    logging.info("Test data shape " + str(np.shape(test_data)) +  str(np.shape(test_y)))

    return train_data, train_y, test_data, test_y

def preprocess_data(concat_data):
    
    LABEL_TO_INDEX = {
        'Iris-virginica': 0,
        'Iris-versicolor': 1,
        'Iris-setosa': 2
    }
    #map categorical values to numbers
    concat_data['species'] = concat_data['species'].map(LABEL_TO_INDEX)
    
    #fix datatypes
    concat_data['sepal_length']= concat_data['sepal_length'].astype('float32')
    concat_data['sepal_width'] = concat_data['sepal_width'].astype('float32')
    concat_data['petal_length'] = concat_data['petal_length'].astype('float32')
    concat_data['petal_width'] = concat_data['petal_width'].astype('float32')
    concat_data['species'] = concat_data['species'].astype('int')
    
    return concat_data