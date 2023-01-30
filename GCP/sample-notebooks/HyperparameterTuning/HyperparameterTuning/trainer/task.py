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

#https://www.kaggle.com/sociopath00/random-forest-using-gridsearchcv
#https://www.kaggle.com/christianlillelund/titanic-using-gridsearchcv-10-classifiers/notebook
#https://www.kaggle.com/ihelon/titanic-hyperparameter-tuning-with-gridsearchcv

def _train_and_evaluate(estimator, features, labels, flags):
    
    
   # Fit the classifer on the tranining set
    estimator.fit(features, labels.values.ravel())

    df = pd.DataFrame.from_dict(estimator.cv_results_)
    df = df.sort_values("mean_test_score", ascending=False)
    logging.info(df)
    logging.info(f"\n\nThe best parameters are {estimator.best_params_} (score = {estimator.best_score_:2f}) \n")
    logging.info(f"The best estimator was {estimator.best_estimator_}" )

    logging.info("*************** Saving the model with best parameters ***************")
    final_model = estimator.best_estimator_

    utils.dump_model(flags.bucket_name, final_model, flags.bucket_folder+'/model/')
    logging.info('saved model!')



def run_experiment(flags):
    
    features, labels = utils.handle_data(flags.preprocessed_file_name, flags.labels_file_name)

    logging.info('data retrieved successfully')
    

    estimator = model.get_estimator(flags)

    _train_and_evaluate(estimator, features, labels, flags)


def _parse_args(argv):
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--preprocessed_file_name', type=str)
    parser.add_argument('--labels_file_name',type=str)
    parser.add_argument('--hyperparameters', type=str)
    parser.add_argument('--n_jobs', type=str)
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