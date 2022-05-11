import os
import time
import pandas as pd
import argparse
from sklearn import __version__ as sklearnver
import joblib

from sklearn.linear_model import LinearRegression
import numpy as np
from fedml_azure import DbConnection
from sklearn.model_selection import train_test_split
import json


# https://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/
############################## Global variables ##############################
with open('config.json', 'r') as f:
    config = json.load(f)
    
feature_columns_names = [
    'Units_Sold', 'Unit_Price', 'Unit_Cost',
       'Total_Revenue', 'Total_Cost']

label_column = 'Total_Profit'

feature_columns_dtype = {
    'Units_Sold': "int64",
    'Unit_Price': "float64",
    'Unit_Cost': "float64",
    'Total_Revenue': "float64",
    'Total_Cost': "float64"}

label_column_dtype = {'Total_Profit': "float64"}

############################## Helper Functions ##############################
def get_data(table_name):
    db = DbConnection()
    start_time = time.time()
    query='select * from '+config['schema']+'.'+table_name
    data = db.execute_query(query)
    print("--- %s seconds ---" % (time.time() - start_time))
    data = pd.DataFrame(data[0], columns=data[1])
    data = data[['Units_Sold', 'Unit_Price', 'Unit_Cost', 'Total_Revenue', 'Total_Cost', 'Total_Profit']]
    return data

############################## Required Functions ##############################
def store_model(model_file_name,model_output):
    print('storing the model....')
    os.makedirs('./outputs', exist_ok=True)
    with open(model_file_name, 'wb') as file:
        joblib.dump(value=model_output, filename='outputs/' + model_file_name)

############################## Training Script Part ##############################

parser = argparse.ArgumentParser()

# AzureML specific arguments. Defaults are set in the environment variables.
parser.add_argument('--model_file_name', type=str)
parser.add_argument('--table_name', type=str)

args = parser.parse_args()

print('\n\n********* Handling Data - Splitting into Train and Test *********n\n')
data = get_data(args.table_name) #getting data from DWC
y = data[label_column]

data.drop(label_column, axis=1, inplace=True)

print(np.shape(data), np.shape(y))

X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.3)

print('\n\n****************************X_train and X_test****************************\n\n')
print(X_train)
print('\n\n')
print(X_test)

print('\n\n****************************y_train and y_test****************************\n\n')
print(y_train)
print('\n\n')
print(y_test)

#Train the LinearRegression model using the fit method
model = LinearRegression().fit(X_train, y_train)

score = model.score(X_test, y_test)

print('\n\n\nScore for fit: ' + str(score) + '\n\n')

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,model)

print("saved model!")
