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
    
    
    train_X = dataset['0']   # '0' corresponds to Texts/Reviews
    train_y = dataset['1'].astype('int')  # '1' corresponds to Label (1 - positive and 0 - negative)
    logging.info(train_X)
    logging.info(train_y)
    
    logging.info('fitting the model...')
    estimator.fit(train_X, train_y)

    utils.dump_model(flags.bucket_name, estimator, 'preprocessed-pipeline/model/')
    logging.info('saved model!')



def run_experiment(flags):
    gcp_data = utils.get_gcp_data(flags.bucket_name, flags.file_path, 'imdb_train.csv')
    dwc_data = utils.get_dwc_data(flags.table_name, float(flags.table_size))
    model_data = pd.concat([gcp_data, dwc_data], axis=0)
    model_data = model_data.head(30000)
    logging.info(model_data.shape)

    logging.info('data retrieved successfully')
    

    estimator = model.get_estimator(flags)

    _train_and_evaluate(estimator, model_data, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--table_name', type=str)
    parser.add_argument('--table_size', type=str)
    parser.add_argument('--file_path')
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
