import argparse
import logging
import os
import sys

import hypertune
import numpy as np
import pandas as pd
from sklearn import model_selection

from trainer import metadata
from trainer import utils
from sklearn.compose import make_column_selector
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline, Pipeline

# https://www.kaggle.com/c/titanic/data <-- Data
# https://johaupt.github.io/scikit-learn/tutorial/python/data%20processing/ml%20pipeline/model%20interpretation/columnTransformer_feature_names.html <-- source for get_features_name function

def _train_and_evaluate(dataset, y_train, flags):
    
    
    # Show the column types we are dealing with
    cat_selector = make_column_selector(dtype_include=object)
    num_selector = make_column_selector(dtype_include=np.number)
    logging.info("\n\nThe following columns are categorical " + str(cat_selector(dataset)))
    logging.info("\nThe following columns are numerical " + str(num_selector(dataset)))

    train_missing_num = dataset[num_selector(dataset)].isnull().any() 
    train_missing_obj = dataset[cat_selector(dataset)].isnull().any() 

    logging.info('\n\ntrain num missing cols:\n' + str(train_missing_num))
    logging.info('\ntrain obj missing cols:\n' + str(train_missing_obj))

    logging.info(dataset['Embarked'].unique())
    em_0=len(dataset[dataset['Embarked']=='S'])
    em_1=len(dataset[dataset['Embarked']=='C'])
    em_2=len(dataset[dataset['Embarked']=='Q'])
    logging.info(str(em_0) + " " + str(em_1) + " " + str(em_2))

    embarked_selector = ['Embarked']
    
    # Handle the Embarked column
    logging.info("\n\n******* Handle the Embarked columns and Use the SimpleImputer to impute values for numerical NaN's and One hot encoder for categories ********")
    mean_embarked = dataset['Embarked'].mode() # S
    logging.info("The category that appears most often in dataset['Embarked'] is " + str(mean_embarked[0]))

    dataset['Embarked'].replace('','-1',inplace=True)
    logging.info(dataset['Embarked'].unique())
    
    
    num_processor = SimpleImputer()
    
    cat_processor = make_pipeline(SimpleImputer(missing_values='-1', strategy='constant', fill_value=mean_embarked[0]), OneHotEncoder(handle_unknown='ignore', sparse=False))
    
    estimator = ColumnTransformer([("num", num_processor, num_selector),("cat", cat_processor, cat_selector)])
    
    transformed_data = estimator.fit_transform(dataset)
    transformed_data = pd.DataFrame(transformed_data)
    transformed_data.columns = utils.get_feature_names(estimator)
    logging.info(transformed_data)
    
    pd.DataFrame(transformed_data).to_csv('transformed_data.csv')
    pd.DataFrame(y_train).to_csv('y_train.csv')
    
    
    logging.info('storing the preprocessed data in output/preprocessed_data.csv ...')
    utils.upload_blob(flags.bucket_name, 'transformed_data.csv','datapreprocessor/output/preprocessed_data.csv')
    
    logging.info('storing the y_train data in output/y_train.csv ...')
    utils.upload_blob(flags.bucket_name, 'y_train.csv', 'datapreprocessor/output/y_train.csv')
    
    # Write model and eval metrics to `output_dir`
    model_output_path = os.path.join(
        flags.job_dir, 'datapreprocessor/model', metadata.MODEL_FILE_NAME)

    utils.dump_model(flags.bucket_name, estimator, 'datapreprocessor/model')
    logging.info('saved model!')



def run_experiment(flags):
    
    model_data = utils.get_dwc_data(flags.table_name)
    logging.info("\n\nThe train dataset shape is: " + str(model_data.shape))
    logging.info("\n\nTrain data:")
    logging.info(model_data.head())
    
    model_data, y_train = utils.handle_data(model_data)

    logging.info('data retrieved successfully')
    

    _train_and_evaluate(model_data, y_train, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--table_name', type=str)
    parser.add_argument('--job-dir', type=str)
    parser.add_argument('--bucket_name', type=str)
    
    return parser.parse_args(argv)


def main():
    """Entry point."""
    logging.info('model starting')

    flags = _parse_args(sys.argv[1:])
    
    logging.basicConfig(level='INFO')
    run_experiment(flags)


if __name__ == '__main__':
    main()
