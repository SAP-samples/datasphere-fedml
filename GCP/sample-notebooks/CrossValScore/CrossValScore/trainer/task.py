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

from sklearn.model_selection import cross_val_score


def _train_and_evaluate(estimator, dataset, flags):
    
    
    train_data, train_y, test_data, test_y = utils.handle_data(dataset)
    logging.info('successfully preprocessed & split data into train and test.')
    
    logging.info('fitting the model...')
    estimator = estimator.fit(train_data, train_y)

    logging.info('\n\n********* Testing *********\n\n')

    scores = cross_val_score(estimator, test_data, test_y, cv=5)
    logging.info('\n\n\nScore for fit:\n')
    logging.info(scores)

    utils.dump_model(flags.bucket_name, estimator, 'crossval/model/')
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
    parser.add_argument('--bucket_name', type=str)
    parser.add_argument('--job-dir', type=str)
    
    return parser.parse_args(argv)


def main():
    """Entry point."""
    logging.info('model starting')

    flags = _parse_args(sys.argv[1:])
    
    logging.basicConfig(level='INFO')
    run_experiment(flags)


if __name__ == '__main__':
    main()
