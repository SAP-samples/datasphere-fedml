# **DwcSagemaker class**

DwcSagemaker class initializes the resources required for the model training, and provides methods that enable the training data to be read from SAP DWC and trains a Machine Learning model on Amazon Sagemaker.

## **Prerequisites**
- `sagemaker>=2`

To update `sagemaker` module, run the following code:

`!pip install --upgrade "sagemaker>=2"`

## **Constructor**

`DwcSagemaker(prefix='model-data', bucket_name=None)`

Initializes AWS specific resources for training such as role, region and bucket name.

If you are using DwcSagemaker on your local machine for predicting an AWS Sagemaker endpoint, please install boto3 and awscli before. `pip install boto3` and follow this documentation to download awscli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### **Parameters**:

`prefix` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
 Prefix for the S3 bucket for temporary storage of training data. Defaults to 'model-data'.      

 `bucket_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
 Name of the S3 bucket for temporary storage of training data. Defaults to None.  If not specified, a default bucket is created for each training job based on the current timestamp.

## **Training a scikit-learn model on Sagemaker**

**`train_sklearn_model(train_data=None, test_data=None, content_type=None, train_script=None, source_dir=None, instance_count=1, instance_type=None, base_job_name=None, hyperparameters=None, wait=False, logs='All', download_output=False)`**

### **Parameters**:

**`train_data` [(pandas.DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) or [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

Training data. This can be one of two types:

- [(pandas.DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) Training data stored in a pandas dataframe.

- [(str)](https://docs.python.org/3/library/stdtypes.html#str) A file:// path in local mode. Accepted file formats are `.csv, .json, .json.gz, .txt`.

**`test_data` [(pandas.DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) or [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

Test data. This can be one of two types:

- [(pandas.DataFrame)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) Test data stored in a pandas dataframe.

- [(str)](https://docs.python.org/3/library/stdtypes.html#str) A file:// path in local mode. Accepted file formats are `.csv, .json, .json.gz, .txt`.

**`content_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

MIME type of the input data. Defaults to None. 

**`train_script` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

Path (absolute or relative) to the Python source file which should be executed as the entry point to training.

**`source_dir` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

Path (absolute, relative or an S3 URI) to a directory with any other training source code dependencies aside from the train_script file. If specified, then train_script must point to a file located at the root of source_dir.

**`instance_count` [(int)](https://docs.python.org/3/library/functions.html#int) (optional):**

Number of Amazon EC2 instances to use for training. Defaults to 1.

**`instance_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):**

Type of EC2 instance to use for training, for example, ‘ml.c4.xlarge’.

**`base_job_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):**

Prefix for training job name when the method launches. If not specified, a default job name is generated based on the training image name and current timestamp.

**`hyperparameters` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) (optional):**

Hyperparameters that will be used for training. Defaults to None. The hyperparameters are made accessible as a dict[str, str] to the training code on SageMaker. For convenience, this accepts other types for keys and values, but `str()` will be called to convert them before training.

**`wait` [(bool)](https://docs.python.org/3/library/functions.html#bool) (optional):**

Whether the call should wait until the job completes. Defaults to True.

**`logs` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):**

A list of strings specifying which logs to print. Acceptable strings are “All”, “None”, “Training”, or “Rules”. To maintain backwards compatibility, boolean values are also accepted and converted to strings. Only meaningful when wait is True.

**`download_output` [(bool)](https://docs.python.org/3/library/functions.html#bool) (optional):** 

Whether the files from `OUTPUT_PATH` should be downloaded on local. Defaults to False

## **Deploying a scikit-learn model on Sagemaker**

**`deploy(clf, initial_instance_count, instance_type, endpoint_name=None, cleanup_resources=True)`**

### **Parameters**:

**`clf` [(Sagemaker SKLearn Estimator)](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/sagemaker.sklearn.html):**

The model to deploy. This is returned from `train_sklearn_model`.

**`initial_instance_count` [(int)](https://docs.python.org/3/library/functions.html#int):**

The initial number of instances to run in the Endpoint created from this Model.

**`instance_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

Type of EC2 instance type to deploy this model to.

**`endpoint_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):**

The name of the endpoint. If not passed, a endpoint name will be generated.

**`cleanup_resources` [(bool)](https://docs.python.org/3/library/functions.html#bool) (optional)**

Whether the data files uploaded to S3 should be deleted. Defaults to True.

## **Invoking a scikit-learn Sagemaker Endpoint**

**`predict(endpoint_name, body, content_type, accept)`**

If you are using this function in your local machine, please install boto3 and awscli before. `pip install boto3` and follow this documentation to download awscli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

After installing awscli, you need to have your environment set up with your correct aws credentials for the default named profile.
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html. For an example of this please refer to LinearRegressionLocalInference.ipynb inside the sample-notebooks/LinearRegression folder on GitHub.

### **Parameters**:

**`endpoint_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The name of the Sagemaker Endpoint to invoke.

**`body` [(bytes or seekable file-like object)](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html)**

Data in the format specified in the `content_type` parameter.
If you have created your own custom input_fn() function, please ensure you are sending the right data values as handled by input_fn.

**`content_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional)**

The MIME type of the input data in the request body.

**`accept` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional)**

The desired MIME type of the inference in the response.

## **Deploying a scikit-learn model on SAP BTP Kyma**
**`deploy_to_kyma(clf, profile_name, initial_instance_count=1, endpoint_name=None, cleanup_resources=True)`**

### **Prerequisites**:

You must have an IAM user that does not have MFA enabled and has EC2 container registry access permissions for pushing and pulling to ecr.
https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html

You must also create a profile using aws cli in jupyterlab that connects to the IAM user with EC2 container registry access permissions. 
The name of this profile is then passed to the function as `profile_name`. Please ensure the region of this profile is the same region as the jupyter instance.
https://docs.aws.amazon.com/cli/latest/reference/configure/index.html

Finally, you also need a Kyma service account and a kubeconfig.yml that specifies the credentials for your Kyma account. 

### **Parameters**:

**`clf` [(str)](https://docs.python.org/3/library/stdtypes.html#str) or [(Sagemaker SKLearn Estimator)](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/sagemaker.sklearn.html)**

The model to deploy. This can either be a string of the name of the training job in AWS Sagemaker Training Jobs, or the estimator object itself.

**`initial_instance_count` [(int)](https://docs.python.org/3/library/functions.html#int):**

The initial number of pods to create in Kyma for this Model. Default is 1.

**`profile_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The name of the profile created using `aws configure --profile <profile_name>` that has the IAM permission to push and pull from ECR.

**`endpoint_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):**

The name of the endpoint. If not passed, a endpoint name will be generated.

**`cleanup_resources` [(bool)](https://docs.python.org/3/library/functions.html#bool) (optional)**

Whether the data files uploaded to S3 should be deleted. Defaults to True.

## **Invoking a Sagemaker scikit-learn endpoint that was deployed on Kyma** 
**`invoke_kyma_endpoint(api, content_type, payload_path=None, payload=None, accept='application/json')`**

### **Parameters**:

**`api` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The api endpoint printed in the console logs from `deploy_to_kyma()`.

**`content_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The content type of data which you are passing. Supported types are `text/csv`, `application/json` and `application/x-npy`

**`payload_path` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The path to which your data is stored. Required if payload is not provided.

**`payload` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The data to which you want to pass to your endpoint for predictions. Required if payload_path is not provided.

**`accept` [(str)](https://docs.python.org/3/library/stdtypes.html#str)**

The content type of data which you are passing. Supported types are `text/csv`, `application/json` and `application/x-npy`. Default is `application/json`
