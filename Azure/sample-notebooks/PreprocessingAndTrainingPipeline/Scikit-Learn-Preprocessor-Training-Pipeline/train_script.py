
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from time import time
from azureml.core import Run

from fedml_azure import DbConnection
import os
import argparse

import joblib

# https://www.kaggle.com/mantri7/imdb-movie-reviews-dataset?select=train_data+%281%29.csv
# https://iq.opengenus.org/naive-bayes-on-tf-idf-vectorized-matrix/z
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
parser.add_argument('--table_size', type=int)
parser.add_argument('--data')

args = parser.parse_args()

run = Run.get_context()
# get input dataset by name
train_dataset = run.input_datasets['train_data']
train_csv = train_dataset.to_pandas_dataframe()

db = DbConnection()
res, column_headers = db.get_data_with_headers(table_name=args.table_name, size=args.table_size)
datasphere_data = pd.DataFrame(res, columns=['0', '1'])

data = pd.concat([train_csv, datasphere_data], axis=0)
data = data.head(30000)
print(data.shape)

train_X = data['0']   # '0' corresponds to Texts/Reviews
train_y = data['1'].astype('int')  # '1' corresponds to Label (1 - positive and 0 - negative)
print(train_X)
print(train_y)

t = time()
vectorizer = TfidfVectorizer()
naive_bayes_classifier = MultinomialNB()

pipeline = Pipeline([('vectorizer', vectorizer), ('naiveBayes', naive_bayes_classifier)])
pipeline.fit(train_X, train_y)
duration = time() - t
print("train time:  %0.3fs" % duration)

print('storing model....')
store_model(args.model_file_name,pipeline)