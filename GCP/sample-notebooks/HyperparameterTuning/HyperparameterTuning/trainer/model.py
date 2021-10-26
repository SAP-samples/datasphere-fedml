from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import json
import logging

def get_estimator(flags):
    N_JOBS=int(flags.n_jobs)
    hyperparameters = json.loads(flags.hyperparameters)
    logging.info("The hyperparameters passed are: ")
    logging.info(str(hyperparameters))

    classifier = GridSearchCV(estimator= RandomForestClassifier(),
                     param_grid=hyperparameters, 
                     refit=True, cv=3,n_jobs=N_JOBS)
    
    return classifier
