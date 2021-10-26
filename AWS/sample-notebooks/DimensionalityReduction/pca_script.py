import argparse
import csv
import json
import joblib
import numpy as np
import pandas as pd
import os

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


feature_columns_names = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst', 'column32']


# https://www.geeksforgeeks.org/implementing-pca-in-python-with-scikit-learn/
# https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
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

############################## Required Functions ##############################
def store_model(model):
    print('storing the model....')
    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    
def store_file(data, name):
    data_output_path = os.path.join(args.output_data_dir, name)
    print("storing the data in {}".format(data_output_path))
    pd.DataFrame(data).to_csv(data_output_path)
    
def model_fn(model_dir):
    """Deserialize fitted model"""
    print('storing the model....')
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

def input_fn(request_body,content_type):
    print('in input_fun')
    if content_type == 'application/json':
        print("content_type is application/json....formatting the request body to a dataframe")
        data = json.loads(request_body)
        data = pd.DataFrame(data)
        return data
    else:
        raise ValueError("This model only supports application/json input")
    
def predict_fn(input_data, model):
    print('in predict_fn')
    result = model.transform(input_data)
    print(type(result))
    return result

############################## Training Script Part ##############################
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--n_components', type=int, default=5)

    args = parser.parse_args()

    print('\n\n********* Handling Data *********n\n')
    data = read_data_arg(args.train, 'train')
    data = data.sample(frac=1).reset_index(drop=True)
    train = data[0:500]
    test = data[500:]
    print('storing the test pca data in output/test_pca_data.csv ...')
    store_file(test,'test_pca_data.csv')
    train.fillna(0, inplace=True)
    print(str(train.shape[0]) + ' rows')
    print(train.head())

    y = train['diagnosis']
    X = train.drop(['diagnosis'], axis=1)

    print(y.shape)
    print(X.shape)


    n_components=int(args.n_components)
    pca = PCA(n_components)
    pca_pipeline = Pipeline([('scaler', StandardScaler()), ('pca', pca)])
    dim_reduction_data = pca_pipeline.fit_transform(X)
    print(dim_reduction_data.shape)
    print(pca.components_)
    print(pca.explained_variance_ratio_)

    print('storing the pca data in output/pca_data.csv ...')
    store_file(dim_reduction_data,'pca_data.csv')

    #Save the model to the location specified by args.model_dir
    store_model(pca_pipeline)

    print("saved model!")


