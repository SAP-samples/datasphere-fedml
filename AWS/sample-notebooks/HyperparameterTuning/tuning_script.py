import argparse
import csv
import json
import joblib
import os

import numpy as np
import pandas as pd
import joblib

#https://www.kaggle.com/sociopath00/random-forest-using-gridsearchcv
#https://www.kaggle.com/christianlillelund/titanic-using-gridsearchcv-10-classifiers/notebook
#https://www.kaggle.com/ihelon/titanic-hyperparameter-tuning-with-gridsearchcv

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from time import time
import sklearn
import ast


############################## Global variables ##############################

features = ['num__PassengerId', 'num__Pclass', 'num__Age', 'num__SibSp',
       'num__Parch', 'num__Fare', 'onehotencoder__x0_female',
       'onehotencoder__x0_male', 'onehotencoder__x1_C', 'onehotencoder__x1_Q',
       'onehotencoder__x1_S']


column_names = ['num__PassengerId', 'num__Pclass', 'num__Age', 'num__SibSp',
       'num__Parch', 'num__Fare', 'onehotencoder__x0_female',
       'onehotencoder__x0_male', 'onehotencoder__x1_C', 'onehotencoder__x1_Q',
       'onehotencoder__x1_S', 'Survived']

############################## Helper Functions ##############################
def read_data_arg(argument, channel):
    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(argument, file) for file in os.listdir(argument) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(argument, channel))

    raw_data = [ pd.read_csv(file, 
                             header=None, 
                             names=column_names ) for file in input_files ]
    
    data = pd.concat(raw_data)
    return data
    
############################## Required Functions ##############################
def model_fn(model_dir):
    """Deserialize fitted model"""
    print('storing the model....')
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

def input_fn(request_body,content_type):
    print('in input_fun')
    if content_type == 'application/json':
        print("content_type is application/json....formatting the request body to a dataframe")
        data = json.loads(request_body)
        data = pd.DataFrame(data)
        return data
    else:
        raise ValueError("This model only supports application/json input")
    
def predict_fn(input_data, model):
    print('in predict_fn')
    result = model.predict(input_data)
    print(type(result))
    return result

    
############################## Training Script Part ##############################
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--max_depth', type=str)
    parser.add_argument('--n_estimators', type=str)
    parser.add_argument('--max_features', type=str)
    parser.add_argument('--min_samples_leaf', type=str)
    parser.add_argument('--n_jobs', type=int)

    args = parser.parse_args()
    print('The scikit-learn version is {}.'.format(sklearn.__version__))

    print('\n\n********* Handling Data *********\n\n')
    train = read_data_arg(args.train, 'train')
    print("training data\n")
    print(train)
    
    X_train = train[features]
    y_train = train['Survived']
    
    print(X_train)
    print(y_train)
    
    N_JOBS=args.n_jobs
    
    
    
    hyperparameters = {
        'max_depth': ast.literal_eval(args.max_depth),
        'n_estimators': ast.literal_eval(args.n_estimators),
        'max_features': ast.literal_eval(args.max_features),
        'min_samples_leaf': ast.literal_eval(args.min_samples_leaf)
        }
    
    print("The hyperparameters passed are: ")
    print(hyperparameters)
    
    classifier = GridSearchCV(estimator= RandomForestClassifier(),
                     param_grid=hyperparameters, 
                     refit=True, cv=3,n_jobs=N_JOBS)

    # Fit the classifer on the tranining set
    classifier.fit(X_train, y_train)

    df = pd.DataFrame.from_dict(classifier.cv_results_)
    df = df.sort_values("mean_test_score", ascending=False)
    print(df)
    print(f"\n\nThe best parameters are {classifier.best_params_} (score = {classifier.best_score_:2f}) \n")
    print(f"The best estimator was {classifier.best_estimator_}" )

    print("*************** Save model with best parameters ***************")
    final_model = classifier.best_estimator_
    #Save the model to the location specified by args.model_dir
    joblib.dump(final_model, os.path.join(args.model_dir, "model.joblib"))

    print("saved model!")



