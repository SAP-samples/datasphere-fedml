import os
import time
import pandas as pd
import json
import platform
import subprocess
import argparse
import sklearn
from sklearn import __version__ as sklearnver
from sklearn import metrics
import joblib



from sklearn.cluster import AgglomerativeClustering
import numpy as np
from fedml_azure import DbConnection


# https://www.kaggle.com/roshansharma/mall-customers-clustering-analysis#Hierarchial-Clustering
# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

############################## Global variables ##############################
with open('config.json', 'r') as f:
    config = json.load(f)
    
feature_columns_names = ['Annual Income (k$)', 'Spending Score (1-100)']


feature_columns_dtype = {
    'Annual Income (k$)': "int64",
    'Spending Score (1-100)': "int64"
    }


############################## Helper Functions ##############################
def get_data(table_name,table_size):
    db = DbConnection()
    data = db.get_data_with_headers(table_name=table_name, size=float(table_size))
    data = pd.DataFrame(data[0], columns=data[1])
    data = data.sample(frac=1).reset_index(drop=True)
    return data.head(100)

############################## Required Functions ##############################
def store_model(model_file_name,model_output):
    print('storing the model....')
    os.makedirs('./outputs', exist_ok=True)
    with open(model_file_name, 'wb') as file:
        joblib.dump(value=model_output, filename='outputs/' + model_file_name)

############################## Training Script Part ##############################

parser = argparse.ArgumentParser()

parser.add_argument('--model_file_name', type=str)
parser.add_argument('--table_name', type=str)
parser.add_argument('--table_size', type=str)

args = parser.parse_args()

print('\n\n********* Handling Data *********n\n')

df = get_data(table_name=args.table_name, table_size=args.table_size)

print(df.shape)

#remove CustomerID column, Genre, and Age column
#retain the Annual Income (in thousands of dollars) and Spending Score (1-100) columns. 
#The Spending Score column signifies how often a person spends money in a mall on a scale of 1 to 100 with 100 being the highest spender.

data = df.iloc[:, 3:5].values

print(data) 

cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
cluster.fit_predict(data)
print(cluster.labels_)

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,cluster)

print("saved model!")
