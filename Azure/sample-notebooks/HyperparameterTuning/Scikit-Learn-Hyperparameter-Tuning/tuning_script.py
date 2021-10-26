#https://www.kaggle.com/sociopath00/random-forest-using-gridsearchcv
#https://www.kaggle.com/christianlillelund/titanic-using-gridsearchcv-10-classifiers/notebook
#https://www.kaggle.com/ihelon/titanic-hyperparameter-tuning-with-gridsearchcv
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from time import time
import sklearn
import os
import argparse
import json

import joblib

############################## Required Functions ##############################
def store_model(model_file_name,model_output):
    print('storing the model....')
    os.makedirs('./outputs', exist_ok=True)
    with open(model_file_name, 'wb') as file:
        joblib.dump(value=model_output, filename='outputs/' + model_file_name)
############################## Helper Functions ##############################
def store_file(data, name):
    os.makedirs('./outputs', exist_ok=True)
    data_output_path = os.path.join('outputs/', name)
    print("storing the data in {}".format(data_output_path))
    pd.DataFrame(data).to_csv(data_output_path)

############################## Training Script Part ##############################
parser = argparse.ArgumentParser()

parser.add_argument('--model_file_name', type=str)
parser.add_argument('--preprocessed_file_name', type=str)
parser.add_argument('--labels_file_name',type=str)
parser.add_argument('--hyperparameters', type=str)
parser.add_argument('--n_jobs', type=int)

args = parser.parse_args()

print('\n\n********* Handling Data *********n\n')

features = pd.read_csv(args.preprocessed_file_name)
features = features.drop(['Unnamed: 0'], axis=1)
print("\n\nThe train features dataset shape is: " + str(features.shape))
print(features.head())


labels = pd.read_csv(args.labels_file_name)
labels = labels.drop(['Unnamed: 0'], axis=1)
print("\n\nThe train labels dataset shape is: " + str(labels.shape))
print(labels.head())

print("\n\n******* Performing Grid Search on Random Forest *******")


N_JOBS=args.n_jobs
hyperparameters = json.loads(args.hyperparameters)
print("The hyperparameters passed are: ")
print(hyperparameters)

classifier = GridSearchCV(estimator= RandomForestClassifier(),
                 param_grid=hyperparameters, 
                 refit=True, cv=3,n_jobs=N_JOBS)

# Fit the classifer on the tranining set
classifier.fit(features, labels.values.ravel())

df = pd.DataFrame.from_dict(classifier.cv_results_)
df = df.sort_values("mean_test_score", ascending=False)
print(df)
print(f"\n\nThe best parameters are {classifier.best_params_} (score = {classifier.best_score_:2f}) \n")
print(f"The best estimator was {classifier.best_estimator_}" )

print("*************** Saving the model with best parameters ***************")
final_model = classifier.best_estimator_

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,final_model)

print("saved model!")

