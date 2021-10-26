import argparse
import csv
import json
import joblib
import numpy as np
import pandas as pd
import os


from sklearn.cluster import AgglomerativeClustering
import numpy as np


# https://www.kaggle.com/roshansharma/mall-customers-clustering-analysis#Hierarchial-Clustering
# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

############################## Global variables ##############################
feature_columns_names = ['Annual Income (k$)', 'Spending Score (1-100)']


feature_columns_dtype = {
    'Annual Income (k$)': "int64",
    'Spending Score (1-100)': "int64"
    }


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
                             names=feature_columns_names ) for file in input_files ]
    
    data = pd.concat(raw_data)
    return data

############################## Optional Specification Functions ##############################
def model_fn(model_dir):
    """Deserialize fitted model"""
    print('storing the model....')
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

def predict_fn(input_data, model):
    print('in predict_fn')
    predictions = model.fit_predict(input_data)
    print(type(predictions))
    return predictions
############################## Training Script Part ##############################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    print('\n\n********* Handling Data *********n\n')

    df = read_data_arg(args.train, 'train')

    print(df.shape)

    #remove CustomerID column, Genre, and Age column
    #retain the Annual Income (in thousands of dollars) and Spending Score (1-100) columns. 
    #The Spending Score column signifies how often a person spends money in a mall on a scale of 1 to 100 with 100 being the highest spender.

    data = df.values

    print(data) 

    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    cluster.fit_predict(data)
    print(cluster.labels_)

    #Save the model to the location specified by args.model_dir
    joblib.dump(cluster, os.path.join(args.model_dir, "model.joblib"))

    print("saved model!")
