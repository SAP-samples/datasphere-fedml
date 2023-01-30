import os
import logging

from hdbcli import dbapi

import pandas as pd
import numpy as np

from sklearn import model_selection
import joblib
# from tensorflow import gfile
import pickle
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


def dump_model(object_to_dump, output_path, flags):
    """Pickle the object and save to the output_path.
    Args:
      object_to_dump: Python object to be pickled
      output_path: (string) output path which can be Google Cloud Storage
    Returns:
      None
    """
        
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(object_to_dump, model_file)
    
    upload_blob(flags.bucket_name, 'model.pkl', output_path+'/model.pkl' )
    

def get_dwc_data(table, size, package_name):
    db = DbConnection(package_name=package_name)
    res, column_headers = db.get_data_with_headers(table_name=table, size=size)
    data = pd.DataFrame(res, columns=column_headers)
    data = data.sample(frac=1).reset_index(drop=True)
    return data
    
def handle_data(data, flags):
    train = data[0:500]
    test = data[500:]
    logging.info(test)
    logging.info('storing the test pca data in output/test_pca_data.csv ...')
    pd.DataFrame(test).to_csv('test_pca_data.csv')
    upload_blob(flags.bucket_name,'test_pca_data.csv', flags.bucket_name+'/output/test_pca_data.csv')
    train.fillna(0, inplace=True)
    logging.info(str(train.shape[0]) + ' rows')
    logging.info(train.head())

    y = train['diagnosis']
    X = train.drop(['diagnosis'], axis=1)

    logging.info(str(y.shape))
    logging.info(str(X.shape))
    
    return X,y