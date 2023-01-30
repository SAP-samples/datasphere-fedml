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

import sklearn
import warnings

    
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
    
    upload_blob(bucket_name, 'model.pkl', output_path+'/model.pkl')
    

def get_dwc_data(table,package_name):
    select_dtypes = {
        'PassengerId': 'int64',
        'Survived': 'int64',
        'Pclass': 'int64',
        'Name': 'object',
        'Sex': 'object',
        'Age': 'float64',
        'SibSp': 'int64',
        'Parch': 'int64',
        'Ticket': 'object',
        'Fare': 'int64',
        'Cabin':'object',
        'Embarked': 'object'
    }

    db = DbConnection(package_name=package_name)
    df = db.execute_query('SELECT * FROM %s' % ('SCE.'+table))
    df = pd.DataFrame(df[0], columns=df[1])
    df.Age.fillna(value=np.nan, inplace=True)
    df = df.astype(select_dtypes)
    return df
    
def handle_data(train):
    
    n=len(train)
    surv_0=len(train[train['Survived']==0])
    surv_1=len(train[train['Survived']==1])

    logging.info("\n\n% of passanger survived in train dataset: " + str(surv_1*100/n))
    logging.info("\n% of passanger not survived in train dataset: " + str(surv_0*100/n))

    logging.info("\n")

    logging.info(train.isnull().sum())

    y_train = train['Survived']
    logging.info("\n\nSurvived values: " + str(y_train.unique()))

    logging.info("***** Dropping columns ... *****")
    train = train.drop(['Survived'], axis=1)
    train = train.drop(['Name', 'Ticket'], axis=1)
    train = train.drop(['Cabin'], axis=1)

    return train, y_train


def get_feature_names(column_transformer):
    """Get feature names from all transformers.
    Returns
    -------
    feature_names : list of strings
        Names of the features produced by transform.
    """
    # Remove the internal helper function
    #check_is_fitted(column_transformer)
    
    # Turn loopkup into function for better handling with pipeline later
    def get_names(trans):
        # >> Original get_feature_names() method
        if trans == 'drop' or (
                hasattr(column, '__len__') and not len(column)):
            return []
        if trans == 'passthrough':
            if hasattr(column_transformer, '_df_columns'):
                if ((not isinstance(column, slice))
                        and all(isinstance(col, str) for col in column)):
                    return column
                else:
                    return column_transformer._df_columns[column]
            else:
                indices = np.arange(column_transformer._n_features)
                return ['x%d' % i for i in indices[column]]
        if not hasattr(trans, 'get_feature_names'):
        # >>> Change: Return input column names if no method avaiable
            # Turn error into a warning
            warnings.warn("Transformer %s (type %s) does not "
                                 "provide get_feature_names. "
                                 "Will return input column names if available"
                                 % (str(name), type(trans).__name__))
            # For transformers without a get_features_names method, use the input
            # names to the column transformer
            if column is None:
                return []
            else:
                return [name + "__" + f for f in column]

        return [name + "__" + f for f in trans.get_feature_names()]
    
    ### Start of processing
    feature_names = []
    
    # Allow transformers to be pipelines. Pipeline steps are named differently, so preprocessing is needed
    if type(column_transformer) == sklearn.pipeline.Pipeline:
        l_transformers = [(name, trans, None, None) for step, name, trans in column_transformer._iter()]
    else:
        # For column transformers, follow the original method
        l_transformers = list(column_transformer._iter(fitted=True))
    
    
    for name, trans, column, _ in l_transformers: 
        if type(trans) == sklearn.pipeline.Pipeline:
            # Recursive call on pipeline
            _names = get_feature_names(trans)
            # if pipeline has no transformer that returns names
            if len(_names)==0:
                _names = [name + "__" + f for f in column]
            feature_names.extend(_names)
        else:
            feature_names.extend(get_names(trans))
    
    return feature_names