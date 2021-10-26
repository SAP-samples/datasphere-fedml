import argparse
import logging
import os
import sys

import numpy as np
import pandas as pd
from sklearn import model_selection

from trainer import metadata
from trainer import model
from trainer import utils

# https://www.geeksforgeeks.org/implementing-pca-in-python-with-scikit-learn/
# https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

def _train_and_evaluate(estimator, X, y, flags):
    
    logging.info('fitting the model...')
    dim_reduction_data = estimator.fit_transform(X)
    logging.info("The shape of the data is " + str(dim_reduction_data.shape))
    
    print('storing the pca data in output/pca_data.csv ...')
    pd.DataFrame(dim_reduction_data).to_csv('data_reduction.csv')
    utils.upload_blob(flags.bucket_name,'data_reduction.csv' , 'dim-red/output/data_reduction.csv' )

    utils.dump_model(estimator, 'dim-red/model', flags)
    logging.info('saved model!')



def run_experiment(flags):
    
    model_data = utils.get_dwc_data(flags.table_name, float(1))
    X,y = utils.handle_data(model_data, flags)

    logging.info('data retrieved successfully')
    

    estimator = model.get_estimator(flags)

    _train_and_evaluate(estimator, X, y, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--table_name', type=str)
    parser.add_argument('--num_components', type=str)
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
