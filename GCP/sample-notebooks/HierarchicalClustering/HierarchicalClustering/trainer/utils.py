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
    
    upload_blob(flags.bucket_name, 'model.pkl', output_path+'model.pkl' )
    

def get_dwc_data(table, size):
    columns_dtype = {
        'Annual Income (k$)': "int64",
        'Spending Score (1-100)': "int64"}
    
    db = DbConnection(package_name='trainer')
    res, column_headers = db.get_data_with_headers(table_name=table, size=size)
    data = pd.DataFrame(res, columns=column_headers)
    data = data.sample(frac=1).reset_index(drop=True)
    return data.astype(columns_dtype).head(100)
    
def handle_data(model_data):

   #remove CustomerID column, Genre, and Age column
    #retain the Annual Income (in thousands of dollars) and Spending Score (1-100) columns. 
    #The Spending Score column signifies how often a person spends money in a mall on a scale of 1 to 100 with 100 being the highest spender.

    model_data = model_data.iloc[:, 3:5].values
    logging.info(model_data)

    return model_data
