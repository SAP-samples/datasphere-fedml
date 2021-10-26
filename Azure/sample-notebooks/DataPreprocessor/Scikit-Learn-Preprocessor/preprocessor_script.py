import numpy as np
import pandas as pd
import joblib
import os
import argparse
from fedml_azure import DbConnection

import sklearn
import warnings

from sklearn.compose import make_column_selector, ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline



#https://www.kaggle.com/c/titanic/data <-- Data
# https://johaupt.github.io/scikit-learn/tutorial/python/data%20processing/ml%20pipeline/model%20interpretation/columnTransformer_feature_names.html <-- source for get_features_name function


############################## Global variables ##############################


features = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']


column_names = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']


select_dtypes = {
    'PassengerId': 'int64',
    'Survived': 'int64',
    'Pclass': 'int64',
    'Name': 'object',
    'Sex': 'object',
    'Age': 'float64',
    'SibSp': 'int64',
    'Parch': 'int64',
    'Ticket': 'object',
    'Fare': 'int64',
    'Cabin':'object',
    'Embarked': 'object'
}

############################## Helper Functions ##############################
def get_feature_names(column_transformer):
    """Get feature names from all transformers.
    Returns
    -------
    feature_names : list of strings
        Names of the features produced by transform.
    """
    # Remove the internal helper function
    #check_is_fitted(column_transformer)
    
    # Turn loopkup into function for better handling with pipeline later
    def get_names(trans):
        # >> Original get_feature_names() method
        if trans == 'drop' or (
                hasattr(column, '__len__') and not len(column)):
            return []
        if trans == 'passthrough':
            if hasattr(column_transformer, '_df_columns'):
                if ((not isinstance(column, slice))
                        and all(isinstance(col, str) for col in column)):
                    return column
                else:
                    return column_transformer._df_columns[column]
            else:
                indices = np.arange(column_transformer._n_features)
                return ['x%d' % i for i in indices[column]]
        if not hasattr(trans, 'get_feature_names'):
        # >>> Change: Return input column names if no method avaiable
            # Turn error into a warning
            warnings.warn("Transformer %s (type %s) does not "
                                 "provide get_feature_names. "
                                 "Will return input column names if available"
                                 % (str(name), type(trans).__name__))
            # For transformers without a get_features_names method, use the input
            # names to the column transformer
            if column is None:
                return []
            else:
                return [name + "__" + f for f in column]

        return [name + "__" + f for f in trans.get_feature_names()]
    
    ### Start of processing
    feature_names = []
    
    # Allow transformers to be pipelines. Pipeline steps are named differently, so preprocessing is needed
    if type(column_transformer) == sklearn.pipeline.Pipeline:
        l_transformers = [(name, trans, None, None) for step, name, trans in column_transformer._iter()]
    else:
        # For column transformers, follow the original method
        l_transformers = list(column_transformer._iter(fitted=True))
    
    
    for name, trans, column, _ in l_transformers: 
        if type(trans) == sklearn.pipeline.Pipeline:
            # Recursive call on pipeline
            _names = get_feature_names(trans)
            # if pipeline has no transformer that returns names
            if len(_names)==0:
                _names = [name + "__" + f for f in column]
            feature_names.extend(_names)
        else:
            feature_names.extend(get_names(trans))
    
    return feature_names

def load_data(table_name):
    db = DbConnection()
    df = db.execute_query('SELECT * FROM %s' % ('SCE.'+table_name))
    df = pd.DataFrame(df[0], columns=df[1])
    df.Age.fillna(value=np.nan, inplace=True)
    df = df.astype(select_dtypes)
    return df

def store_file(data, name):
    os.makedirs('./outputs', exist_ok=True)
    data_output_path = os.path.join('outputs/', name)
    print("storing the data in {}".format(data_output_path))
    pd.DataFrame(data).to_csv(data_output_path)
    
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

args = parser.parse_args()

print('\n\n********* Handling Data *********n\n')

train = load_data(args.table_name)
print("\n\nThe train dataset shape is: " + str(train.shape))
print("\n\nTrain data:")
print(train.head())
#We have 11 feature columns and target variable Survived which is binary.

#Pclass, Sex and Embarked are Categorical Features
# Age, SibSp, Parch and Fare are continuous variables.

n=len(train)
surv_0=len(train[train['Survived']==0])
surv_1=len(train[train['Survived']==1])

print("\n\n% of passanger survived in train dataset: ",surv_1*100/n)
print("\n% of passanger not survived in train dataset: ",surv_0*100/n)

print("\n")

print(train.isnull().sum())

y_train = train['Survived']
print("\n\nSurvived values: " + str(y_train.unique()))

print("*** Dropping columns ... *****")
train = train.drop(['Survived'], axis=1)
train = train.drop(['Name', 'Ticket'], axis=1)
train = train.drop(['Cabin'], axis=1)

# Show the column types we are dealing with
cat_selector = make_column_selector(dtype_include=object)
num_selector = make_column_selector(dtype_include=np.number)
print("\n\nThe following columns are categorical " + str(cat_selector(train)))
print("\nThe following columns are numerical " + str(num_selector(train)))

train_missing_num = train[num_selector(train)].isnull().any() 
train_missing_obj = train[cat_selector(train)].isnull().any() 

print('\n\ntrain num missing cols:\n' + str(train_missing_num))
print('\ntrain obj missing cols:\n' + str(train_missing_obj))

print(train['Embarked'].unique())
em_0=len(train[train['Embarked']=='S'])
em_1=len(train[train['Embarked']=='C'])
em_2=len(train[train['Embarked']=='Q'])
print(em_0, em_1, em_2)

embarked_selector = ['Embarked']

# Handle the Embarked column
print("\n\n******* Handle the Embarked columns and Use the SimpleImputer to impute values for numerical NaN's and One hot encoder for categories ********")
mean_embarked = train['Embarked'].mode() # S
print("The category that appears most often in train['Embarked'] is ", mean_embarked[0])

train['Embarked'].replace('','-1',inplace=True)
print(train['Embarked'].unique())

# Use the SimpleImputer to impute values for numerical NaN's and One hot encoder for categories
num_processor = SimpleImputer()
cat_processor = make_pipeline(SimpleImputer(missing_values='-1', strategy='constant', fill_value=mean_embarked[0]), OneHotEncoder(handle_unknown='ignore', sparse=False))
transformer = ColumnTransformer([("num", num_processor, num_selector),("cat", cat_processor, cat_selector)])

transformed_data = transformer.fit_transform(train)
transformed_data = pd.DataFrame(transformed_data)
transformed_data.columns = get_feature_names(transformer)
print(transformed_data)

print('storing the preprocessed data in preprocessed_data.csv ...')

store_file(transformed_data,'preprocessed_data.csv')
store_file(y_train, 'labels.csv')

#Save the model to the location specified by args.model_dir
store_model(args.model_file_name,transformer)

print("saved model!")



