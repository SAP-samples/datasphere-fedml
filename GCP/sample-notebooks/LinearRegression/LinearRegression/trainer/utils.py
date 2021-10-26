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
#     with open(output_path, 'wb') as model_file:
#           pickle.dump(object_to_dump, model_file)
#     if not gfile.Exists(output_path):
#         gfile.MakeDirs(os.path.dirname(output_path))
#     with gfile.Open(output_path, 'w') as wf:
#         joblib.dump(object_to_dump, wf)
        
    with open('model.pkl', 'wb') as model_file:
      pickle.dump(object_to_dump, model_file)
    
    upload_blob(flags.bucket_name, 'model.pkl', output_path+'model.pkl' )
    

def get_dwc_data(table, size):
    columns_dtype = {
    'Units_Sold': "int64",
    'Unit_Price': "float64",
    'Unit_Cost': "float64",
    'Total_Revenue': "float64",
    'Total_Cost': "float64",
    'Total_Profit': "float64"}
    
    db = DbConnection(package_name='trainer')
    res, column_headers = db.get_data_with_headers(table_name=table, size=size)
    data = pd.DataFrame(res, columns=column_headers)
    data = data[['Units_Sold', 'Unit_Price', 'Unit_Cost', 'Total_Revenue', 'Total_Cost', 'Total_Profit']]
    return data.astype(columns_dtype)
    
def split_data(model_data):
    
    y = model_data['Total_Profit']

    model_data.drop('Total_Profit', axis=1, inplace=True)

    logging.info("The shape of model data is "+ str(np.shape(model_data)))
    logging.info("The shape of y is " + str(np.shape(y)))

    X_train, X_test, y_train, y_test = train_test_split(model_data, y, test_size=0.3)
    
    logging.info('\n\n****************************X_train and X_test****************************\n\n')
    logging.info(X_train)
    logging.info('\n\n')
    logging.info(X_test)

    logging.info('\n\n****************************y_train and y_test****************************\n\n')
    logging.info(y_train)
    logging.info('\n\n')
    logging.info(y_test)


    return X_train, X_test, y_train, y_test
