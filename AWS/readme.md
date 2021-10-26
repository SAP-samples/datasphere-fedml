# **DwcSagemaker class**

DwcSagemaker class initializes the resources required for the model training, and provides methods that enable the training data to be read from SAP DWC and trains a Machine Learning model on Amazon Sagemaker.

## **Constructor**

`DwcSagemaker(prefix=None, bucket_name=None)`

Initializes AWS specific resources for training such as role, region and bucket name

### **Parameters**:

`prefix` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
 Prefix for the S3 bucket for temporary storage of training data. Defaults to None.      

 `bucket_name` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
 Name of the S3 bucket for temporary storage of training data. Defaults to None.  If not specified, a default bucket is created for each training job based on the current timestamp.

## **Training a scikit-learn model on Sagemaker**

**`train_sklearn_model(train_data=None, test_data=None, content_type=None, train_script=None, instance_count=1, instance_type=None, base_job_name=None, hyperparameters=None, wait=False, logs='All', download_output=False)`**

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
