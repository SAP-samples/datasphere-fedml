import argparse
import logging
import os
import sys

import hypertune
import numpy as np
import pandas as pd
from sklearn import model_selection

from trainer import metadata
from trainer import model
from trainer import utils

# https://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/

def _train_and_evaluate(estimator, dataset, flags):
    
    
    X_train, X_test, y_train, y_test = utils.split_data(dataset)
    logging.info('successfully data split into train and test.')
    
    logging.info('fitting the model...')
    estimator = estimator.fit(X_train, y_train)


    score = estimator.score(X_test, y_test)
    logging.info('\n\n\nScore for fit: ' + str(score) + '\n\n')

    # Write model and eval metrics to `output_dir`

    utils.dump_model(estimator, 'linear/model/', flags)
    logging.info('saved model!')



def run_experiment(flags):
    
    model_data = utils.get_dwc_data(flags.table_name, float(flags.table_size))

    logging.info('data retrieved successfully')
    

    estimator = model.get_estimator(flags)

    _train_and_evaluate(estimator, model_data, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--table_name', type=str)
    parser.add_argument('--table_size', type=str)
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
