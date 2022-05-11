import pandas as pd
import numpy as np
import os
import argparse

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from fedml_azure import DbConnection

import joblib

# https://www.geeksforgeeks.org/implementing-pca-in-python-with-scikit-learn/
# https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
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
parser.add_argument('--n_components', type=str)

args = parser.parse_args()

print('\n\n********* Handling Data *********n\n')

db = DbConnection()
res, column_headers = db.get_data_with_headers(table_name=args.table_name, size=1)
data = pd.DataFrame(res, columns=column_headers)
data = data.sample(frac=1).reset_index(drop=True)
train = data[0:500]
train.fillna(0, inplace=True)
print(str(train.shape[0]) + ' rows')
print(train.head())

y = train['diagnosis']
X = train.drop(['diagnosis'], axis=1)

print(y.shape)
print(X.shape)


n_components=int(args.n_components)
pca = PCA(n_components)
pca_pipeline = Pipeline([('scaler', StandardScaler()), ('pca', pca), ('classifier', LogisticRegression())])
pca_pipeline.fit(X, y)

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,pca_pipeline)

print("saved model!")


