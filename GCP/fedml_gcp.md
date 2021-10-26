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
