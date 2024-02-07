# **fedml_gcp**

Please make sure the libraries in your setup.py for training and requirements.txt for custom predictions are supported by the Python version you are using.

# **DwcGCP class**

DwcGCP class initializes the resources required for the model training, enables the training data to be read from SAP Datasphere in real time without storing it in any GCP Storage, trains a Machine Learning model and deploys it on the Google Cloud Platform.

## **Constructor**

`DwcGCP(configs={})`

Initializes the DwcGCP class and initializes the Vertex AI SDK.


#### **Parameters**:

**`configs` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
Dictionary with key-value pairs of the parameter defined [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform#google_cloud_aiplatform_init)


## **Upload Training Package to Cloud Storage Bucket**

**`make_tar_bundle(output_filename='training.tar.gz', source_dir='training', destination='train/training.tar.gz')`**

#### **Parameters**:

**`output_filename` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (required):**
Name of output tar bundle. Default: 'training.tar.gz'

**`source_dir` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (required):**
Path to local training application directory. Default: 'training'

**`destination` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (required):**
GCP Cloud Storage destination path. Default: 'train/training.tar.gz'


## **Training a model on Google Vertex AI**

**`train_model(training_inputs, training_type='custom', params={})`**
Note: please ensure you are using a training image that is currently supported by GCP.
#### **Parameters**:

**`training_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (required):**
two values supported - 'custom' and 'customPythonPackage'. Defaults to 'custom'.

If 'custom' is provided, then the `training_inputs` should match the training inputs for a CustomTrainingJob in Vertex AI. 

In addition, if using 'custom' and getting data from SAP Datasphere in your training script, you will need to do the following:
1. upload the config.json to the GCS bucket you specified to the DwcGCP constructor.
2. In your training script, where you are creating the instance of DbConnection, you will need to use the url parameter and pass url='/gcs/'+bucket_name+'/config.json', where bucket_name is one of the cmd arguments you passed to the args parameter in `params`.

If 'customPythonPackage' is provided, then `training_inputs` should match the training inputs for a CustomPythonPackageTrainingJob in Vertex AI. 

**`training_inputs` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
Dictionary of training inputs as defined by Vertex AI.

If you used 'custom' in `training_type`, please refer [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomTrainingJob) for the dictionary key-value pairs. display_name, script_path, and container_uri are required.

If you used 'customPythonPackage' in `training_type`, please refer [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomPythonPackageTrainingJob) for the dictionary key-value pairs. display_name, python_package_gcs_uri, python_module_name and container_uri are required.

**`params` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
dictionary of the parameters to run the training job with. Defaults to None. 

For `custom` please refer [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomTrainingJob#google_cloud_aiplatform_CustomTrainingJob_run) for the specifics on what values can be used in the dictionary. 

For `customPythonPackage` - please refer [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomPythonPackageTrainingJob#google_cloud_aiplatform_CustomPythonPackageTrainingJob_run) for the specifics on what values can be used in the dictionary. 

## **Create an Endpoint in Vertex AI**

Optional step to create an endpoint with your specifications. You can deploy a model to this endpoint using the deploy function, or you can use deploy as is and deploy will create an endpoint for you.

**`create_or_get_endpoint(endpoint_config={}, create_endpoint=True)`**

#### **Parameters**:

**`create_endpoint` [(bool)](https://docs.python.org/3/library/functions.html#bool) (required):**
True says you want to create a new endpoint.
False says you want to get an existing endpoint.

**`endpoint_config` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**

If `create_endpoint` is True, endpoint_config key-value pairs should match those from the arguments listed [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint#google_cloud_aiplatform_Endpoint_create)

If `create_endpoint` is False, endpoint_config key-value pairs should match those from the arguments listed [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint)


## **Deploy model to Vertex AI**

**`deploy(model, model_config={}})`**
Note: please ensure you are using a deploy image that is currently supported by GCP.
#### **Parameters**:

**`model` [(str)](https://docs.python.org/3/library/stdtypes.html#str) or [(aiplatform.Model)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model) (required):**
If passing a string, `model` should be fully-qualified model resource name or model ID. Otherwise, `model` should be a Model object.
If you are using a custom prediction routine, you will need to perform `upload_custom_predictor` before this function (see function definition below), and then call deploy using the model returned from `upload_custom_predictor`. If you are using the default prediction routine, use this `deploy` function on the model you want to deploy (i.e. the model returned from `train_model`).

**`model_config` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
A dictionary, whose key-value pairs are the parameters as defined [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model#google_cloud_aiplatform_Model_deploy)


### **Using a Custom Prediction Routine**

This is a function you will use before deploy ONLY if you are creating your own custom prediction routine.

For information on how to create a custom prediction routine and the files needed, please refer [(here)](https://cloud.google.com/vertex-ai/docs/predictions/custom-prediction-routines).

In summary, you need to have a folder with a Predictor python file that implementes the google.cloud.aiplatform.prediction.handler.predictor interface and if you would like, an optional Handler python file that implements the google.cloud.aiplatform.prediction.handler.Handler interface. You will also need to have a requirements.txt file in this folder that specified ALL dependencies. You should not assume that it will work on the docker image. All dependencies need to be specified.

Before running this function, you will also need to import your predictor class as such `from <folder>.<file> import MyPredictor`

**`upload_custom_predictor(cpr_model_config, upload_config={})`**

You may need to authenticate first in the Vertex AI Notebook Instance terminal using `gcloud auth login`

#### **Parameters**:

**`cpr_model_config` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
A dictionary with the key-value pairs are parameters as defined [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalModel#google_cloud_aiplatform_prediction_LocalModel_build_cpr_model)

**`upload_config` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
A dictionary with the key-value pairs are the parameters as defined [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model#google_cloud_aiplatform_Model_upload). Do NOT provide local_model. This function creates the local model and will automatically handle the custom prediction routine model creation and uploading for you.

## **Invoke Predictions from a Vertex AI Endpoint**

**`predict(endpoint, predict_params)`**

**`endpoint` [(str)](https://docs.python.org/3/library/stdtypes.html#str) or [(aiplatform.Endpoint)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint) (required):**
If passing a string, `endpoint` should be fully-qualified endpoint resource name or endpoint ID. Otherwise, `endpoint` should be a Model object.

**`predict_params` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (required):**
A dictionary with key-value pairs representing the parameters as defined in the predict method [(here)](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint#google_cloud_aiplatform_Endpoint_predict)


## **Release Notes**

FedML GCP 2.1.0 now fully supports Vertex AI, with the exception of SAP BTP Kyma Deployment.