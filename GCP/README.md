# **DwcGCP class**

DwcGCP class initializes the resources required for the model training, enables the training data to be read from SAP DWC in real time without storing it in any GCP Storage, trains a Machine Learning model and deploys it on the Google Cloud Platform .

## **Constructor**

`DwcGCP(project_name=None, bucket_name=None)`

Initializes the DwcGCP class with GCP project configurations

Project Name:

- An existing GCP project name: project id assinged in GCP console.

Bucket Name:

- An existing GCP Cloud Storage Bucket name.

### **Parameters**:

`project_name` [(string)](https://cloud.google.com/resource-manager/docs/creating-managing-projects) (required):  
 Assigns an existing GCP project name. Defaults to None.

`bucket_name` [(string)](https://cloud.google.com/storage/docs/naming-buckets) (required):  
 Assigns an existing GCP Cloud Storage Bucket name. Defaults to None.

# **Training a model on GCP**

### **Upload Training Package to Cloud Storage Bucket**

` make_tar_bundle(output_filename='training.tar.gz', source_dir='training', destination='train/training.tar.gz')`

- `output_filename` [(string)] (required):  
  Name of output tar bundle. Default: 'trainging.tar.gz'

- `source_dir` [(string)] (required):  
  Path to local training application directory. Default: 'training'

- `destination` [(string)] (required):  
  GCP Cloud Storage destination path. Default: 'train/training.tar.gz'

### **Submit Training Job to AI Platform**

`train_model(jobId, training_inputs)`

- `jobId` [(string)] (required):  
  Unique JobId chosen by developer. Must be distinct from all previous training jobs. Example: 'trainging_job_1'

- `training_inputs` [(dict)] (https://cloud.google.com/ai-platform/training/docs/training-jobs) (required):  
  Dictionary of training inputs for Google Training Job. Include Cloud Storage path to DwcGCP library (whl file stored in cloud storage) in packages_uri field.

"""

### **Deploy model to AI Platform**

`deploy(model_name, model_location, version, region, prediction_location='', custom_predict=None, module_name=None, onlinePredictionLogging=False, onlinePredictionConsoleLogging=False)`

- `model_name` [(string)] (required):  
  Unique model_name chosen by developer. Example: 'model_1'

- `model_location` [(string)] (required):  
  Path to saved model file in Google Cloud Storage.

- `version` [(string)] (required):  
  Unique model_name chosen by developer. Example: 'version_1'

- `region` [(string)] (required):  
  Google compute region in which developer would like model deployed. Example: 'us-east1'

- `prediction_location` [(string)] (optional):  
  If using a custom prediction routine the path to the prediction package. More information can be found here (https://cloud.google.com/ai-platform/prediction/docs/custom-prediction-routines).

- `custom_predict` [(boolean)] (optional):  
  Set to `True` if using custom prediction module.

- `module_name` [(string)] (optional):  
  Name of module in prediction package. Example 'predictor.MyPredictor'

- `onlinePredictionConsoleLogging` [(boolean)] (optional):  
  Set to `True` too log prediction routine in the console logger.

### **Invoke Predictions from AI Platform Endpoint**

`predict(data, model_name)`

- `data` [(dict)] (required):  
  Data in dictionary format. Values in list format and key 'Instances'. Example: `data = {'instances':[[...], [...]]}`

- `model_name` [(string)] (required):  
  Name of model deployed on AI Platform that you would like to invoke.

### **Deploying a model on SAP BTP Kyma**

**Prerequisites**:

You must have a GCP service account with the correct priviliges for Container Registry, Cloud Storage and AI Platform. Download the service account key as a JSON and upload to your development environment. More information can be found here (https://cloud.google.com/iam/docs/service-accounts).

`deploy_to_kyma(profile_name, key_file, image_name, custom_predictor=None, download_model=True, model_location=None, initial_instance_count=1)`

- `profile_name` [(string)] (required):  
  Service account username.

- `key_file` [(string)] (required):  
  Path to JSON key file in your environment. See above for more information on creation of the key file.

- `image_name` [(string)] (required):  
  A unique name for your image. This will be used for the Kyma pod as well. No camel case (\_) allowed.

- `custom_predictor` [(string)] (optional):  
  If using a custom prediction routine the developer must provide a path to the prediction class file.

- `download_model` [(boolean)] (optional):  
  Default `True`. Set to false if model file is already in local directory in your development environment.

- `model_location` [(string)] (optional):  
  If `download_model` is set to `True` developer must provide path to the model file in Cloud Storage to download the model file to the local environment.

- `initial_instance_count` [(int)] (optional):  
  The initial number of pods to create in Kyma for this Model. Default is 1.

### **Invoke Model Endpoint on SAP BTP Kyma**

`invoke_kyma_endpoint(api, payload_path=None)`

- `api` [(string)] (required):  
  The api endpoint printed in the console logs from `deploy_to_kyma()`.

- `payload_path` [(string)] (required):
  Path to JSON file containing data upon which you would like to run predictions i.e. 'sample_data.json'. At this time only JSON format is supported. Data must be in format of `{'instances':[[...], [...]]}` similar to how GCP AI Platfrom accepts prediction requests.

"""
