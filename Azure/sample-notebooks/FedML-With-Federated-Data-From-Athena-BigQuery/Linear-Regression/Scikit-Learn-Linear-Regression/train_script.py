import os,json
import pandas as pd
import argparse,joblib

from sklearn.linear_model import LinearRegression
import numpy as np
from fedml_azure import DbConnection
from sklearn.model_selection import train_test_split

############################## Global variables ##############################
with open('config.json', 'r') as f:
    config = json.load(f)

label_column = 'total_profit'


##############################  Function to read the federated data from Athena and BigQuery via SAP Data Warehouse Cloud ##############################
def get_data(table_name):
    db = DbConnection()
    query='select * from '+config['schema']+'.'+table_name
    #The DbConnection.execute_query() method queries the table/view from SAP Data Warehouse Cloud.
    data = db.execute_query(query)
    data = pd.DataFrame(data[0], columns=data[1])
    data=data[['units_sold', 'unit_price', 'unit_cost','total_revenue', 'total_cost','total_profit']]
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