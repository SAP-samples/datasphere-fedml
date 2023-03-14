import os
import time
import pandas as pd
import argparse
from sklearn import __version__ as sklearnver
import joblib


from sklearn.linear_model import LogisticRegression
import numpy as np
from fedml_azure import DbConnection
from sklearn.model_selection import train_test_split

############################## Global variables ##############################

# Dictionary to convert labels to indices
LABEL_TO_INDEX = {
    'Iris-virginica': 0,
    'Iris-versicolor': 1,
    'Iris-setosa': 2
}

# Dictionary to convert indices to labels
INDEX_TO_LABEL = {
    0: 'Iris-virginica',
    1: 'Iris-versicolor',
    2: 'Iris-setosa'
}

feature_columns_names = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]
feature_columns_dtype = {
    'sepal_length':'float32',
    'sepal_width':'float32',
    'petal_length':'float32',
    'petal_width':'float32'
}

label_column = 'species'
label_column_dtype = {
    'species':'string'
}

############################## Helper Functions ##############################
def get_data(table_name,table_size):
    db = DbConnection()
    data = db.get_data_with_headers(table_name=table_name, size=int(table_size))
    data = pd.DataFrame(data[0], columns=data[1])
    return data

def preprocess_data(concat_data):
    
    #map categorical values to numbers
    concat_data['species'] = concat_data['species'].map(LABEL_TO_INDEX)
    
    #fix datatypes
    concat_data['sepal_length']= concat_data['sepal_length'].astype('float32')
    concat_data['sepal_width'] = concat_data['sepal_width'].astype('float32')
    concat_data['petal_length'] = concat_data['petal_length'].astype('float32')
    concat_data['petal_width'] = concat_data['petal_width'].astype('float32')
    concat_data['species'] = concat_data['species'].astype('int')
    
    return concat_data

    
############################## Required Functions ##############################
def store_model(model_file_name,model_output):
    print('storing the model....')
    os.makedirs('./outputs', exist_ok=True)
    with open(model_file_name, 'wb') as file:
        joblib.dump(value=model_output, filename='outputs/' + model_file_name)


############################## Training Script Part ##############################

# Create a parser object to collect the environment variables that are in the
parser = argparse.ArgumentParser()

# Arguments we passed in training function. I am passing training and testing data to this script.
parser.add_argument('--model_file_name', type=str)
parser.add_argument('--table_name', type=str)
parser.add_argument('--table_size', type=str)
args = parser.parse_args()

print('\n\n********* Handling Data - Splitting into Train and Test *********n\n')
data = get_data(args.table_name, args.table_size) #getting data from SAP Datasphere

# Shuffling the dataframe to get a more representative sample, then using only the top 100 records for train and test
data = data.sample(frac=1).reset_index(drop=True)
sub_data = data.head(100)

#saving 101-150 in inference_data.csv for testing the inference.
inference_data = data[101:]
inference_data.to_csv('inference_data.csv')

#splitting the data in to X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = train_test_split(sub_data.drop(['species'], axis=1), sub_data['species'], test_size=0.3)

#getting the train data together
train_data = pd.concat([X_train, y_train], axis=1)
print('\n******** Train Data ********\n')
print(train_data.head())

#getting the test data together
test_data = pd.concat([X_test, y_test], axis=1)
print('\n******** Test Data ********\n')
print(test_data.head())

# preprocess train data - convert categorical to numerical
train_data = preprocess_data(train_data)
print('\n******** Preprocessed Train data:********\n')
print(train_data.head())

# train Y column
train_y = train_data['species']

# train X columns
train_data.drop(['species'], axis=1, inplace=True)


print(np.shape(train_data), np.shape(train_y))


print('\n\n********* Training *********n\n')
#Train the LogisticRegression model using the fit method
model = LogisticRegression().fit(train_data, train_y)

print('\n\n********* Testing *********n\n')

# preprocess test data - convert categorical to numerical
test_data = preprocess_data(test_data)
print('\n******** Preprocessed Test data:********\n')
print(test_data.head())

# test Y column
test_y = test_data['species']

# test X columns
test_data.drop(['species'], axis=1, inplace=True)


print(np.shape(test_data), np.shape(test_y))

score = model.score(test_data, test_y)
print('The model score is: ' + str(score))

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,model)

print('saved model!')
