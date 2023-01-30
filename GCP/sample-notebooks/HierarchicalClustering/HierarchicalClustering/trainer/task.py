import argparse
import logging
import os
import sys

import hypertune
import numpy as np
import pandas as pd
from sklearn import model_selection

from trainer import model
from trainer import utils

# https://www.kaggle.com/roshansharma/mall-customers-clustering-analysis#Hierarchial-Clustering
# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

def _train_and_evaluate(estimator, dataset, flags):
    
    logging.info('fitting the model...')
    estimator.fit_predict(dataset)
    logging.info("The estimator labels are " + str(estimator.labels_))

    utils.dump_model(estimator, flags.bucket_folder+'/model/', flags)
    logging.info('saved model!')



def run_experiment(flags):
    
    model_data = utils.get_dwc_data(flags.table_name, float(flags.table_size), flags.package_name)
    model_data = utils.handle_data(model_data)

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
    parser.add_argument('--bucket_folder', type=str)
    parser.add_argument('--package_name', type=str)
    
    return parser.parse_args(argv)


def main():
    """Entry point."""
    logging.info('model starting')

    flags = _parse_args(sys.argv[1:])
    
    logging.basicConfig(level='INFO')
    run_experiment(flags)


if __name__ == '__main__':
    main()