import argparse
import logging
import os
import sys

import hypertune
import numpy as np
import pandas as pd
from sklearn import model_selection
from google.cloud import storage
from fedml_gcp import DbConnection
from sklearn.model_selection import train_test_split

import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def get_estimator(flags):
    vectorizer = TfidfVectorizer()
    naive_bayes_classifier = MultinomialNB()
    pipeline = Pipeline([('vectorizer', vectorizer), ('naiveBayes', naive_bayes_classifier)])

    return pipeline

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
    
def get_gcp_data(bucket_name, source_blob_name, destination_file_name):
    download_blob(bucket_name, source_blob_name, destination_file_name)
    return pd.read_csv(destination_file_name)
    
def download_blob(bucket_name, source_blob_name, destination_file_name):
     

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)

        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        print(
            "Downloaded storage object {} from bucket {} to local file {}.".format(
                source_blob_name, bucket_name, destination_file_name
            )
        )
        
def get_dwc_data(table, size, bucket_name):
    db = DbConnection(url='/gcs/'+bucket_name+'/config.json')
    res, column_headers = db.get_data_with_headers(table_name=table, size=size)
    data = pd.DataFrame(res, columns=['0', '1'])
    return data
    
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

def _train_and_evaluate(estimator, dataset, flags):
    
    
    train_X = dataset['0']   # '0' corresponds to Texts/Reviews
    train_y = dataset['1'].astype('int')  # '1' corresponds to Label (1 - positive and 0 - negative)
    logging.info(train_X)
    logging.info(train_y)
    
    logging.info('fitting the model...')
    estimator.fit(train_X, train_y)

    dump_model(flags.bucket_name, estimator, flags.bucket_folder+'/model/')
    logging.info('saved model!')



def run_experiment(flags):
    gcp_data = get_gcp_data(flags.bucket_name, flags.file_path, 'imdb_train.csv')
    dwc_data = get_dwc_data(flags.table_name, float(flags.table_size), flags.bucket_name)
    model_data = pd.concat([gcp_data, dwc_data], axis=0)
    model_data = model_data.head(30000)
    logging.info(model_data.shape)

    logging.info('data retrieved successfully')
    

    estimator = get_estimator(flags)

    _train_and_evaluate(estimator, model_data, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--table_name', type=str)
    parser.add_argument('--table_size', type=str)
    parser.add_argument('--file_path')
    parser.add_argument('--job-dir', type=str)
    parser.add_argument('--bucket_name', type=str)
    parser.add_argument('--bucket_folder', type=str)
    
    return parser.parse_args(argv)


def main():
    """Entry point."""
    logging.info('model starting')

    flags = _parse_args(sys.argv[1:])
    
    logging.basicConfig(level='INFO')
    run_experiment(flags)


if __name__ == '__main__':
    main()