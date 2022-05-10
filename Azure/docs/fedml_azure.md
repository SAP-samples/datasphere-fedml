# **Methods to create resources for training a model in AzureML**

[create_workspace](#create_workspace)  
Method to get an existing workspace.

[create_compute](#create_compute)  
Method to create a new compute or obtain an existing compute.

[create_environment](#create_environment)  
Method to create a new environment or obtain an existing environment.

## **create_workspace**  
Method to get an existing workspace.

`create_workspace(workspace_args)` 

### **Parameters**:

`workspace_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted workspace_args dictionary keyworded arguments](parameters.md#workspace_args-dictionary-keyworded-arguments):  
  A dictionary of keyword args to get an existing workspace. 

### **Returns**

Workspace

### **Return Type**

[Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py)

### **Remarks**
Example: Getting the existing workspace

```
workspace=create_workspace(workspace_args={"subscription_id": <subscription_id>,  
                                           "resource_group": <resource_group>,  
                                           "workspace_name": <workspace_name>  
                                            }
                          )
```
## **create_compute**  
Method to create a new compute or obtain an existing compute

`create_compute(workspace,compute_type,compute_args)`

### **Parameters**  :

`workspace` [(azureml.core.Workspace)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py):  
 Assigns an existing Workspace object.  

`compute_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str):  
Type of compute to be created. The following compute_type are supported:
 - `'AmlComputeCluster'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.AmlCompute'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)?view=azure-ml-py#:~:text=An%20Azure%20Machine%20Learning%20Compute%20(AmlCompute)%20is%20a%20managed%2D,be%20shared%20with%20other%20users.).  

 - `'AmlComputeInstance'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.ComputeInstance'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.computeinstance(class)?view=azure-ml-py).  

  - `'AKS'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.aks'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.aks?view=azure-ml-py).         

`compute_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted compute_args dictionary keyworded arguments](parameters.md#compute_args-dictionary-keyworded-arguments):  
A dictionary of keyword args to create a new Compute or get an existing Compute.

### **Returns**

Compute

### **Return Type**

[Compute](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute?view=azure-ml-py)

### **Remarks**  
Example: Creation of a new compute with compute_type 'AmlComputeCluster'

```
compute=create_compute(workspace=<workspace-object>,
                     compute_type='AmlComputeCluster',
                     compute_args={'vm_size':'Standard_D12_v2',
                              'vm_priority':'lowpriority',
                              'compute_name':<compute-name>,
                              'min_nodes':0,
                              'max_nodes':4,
                              }
                )
```

Example: Creation of a new compute with compute_type 'AmlComputeInstance'

```
compute=create_compute(workspace=<workspace-object>,
                     compute_type='AmlComputeInstance',
                     compute_args={
                          'vm_size':"Standard_D3_v2",
                          'compute_name':<compute-name>
                      }
                )
```

Example: Creation of a new compute with compute_type 'AKS'  

```
compute=create_compute(workspace=<workspace-object>,
                   compute_type='AKS',
                   compute_args={'compute_name':<compute-name>})
```  

## **create_environment**  
Method to create a new environment or obtain an existing environment

`create_environment(workspace,environment_type,environment_args)`

### **Parameters**:

`workspace` [(azureml.core.Workspace)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py):  
 Assigns an existing Workspace object.  

`environment_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str):  
Specifies the method of creating an environment.The following environment_type are supported:
 - `'CondaPackageEnvironment'` for creating a new Environment or obtaining an existing environment by specifying pip, conda and private wheel dependency.
 - `'CondaSpecificationEnvironment'` for creating a new Environment or obtaining an existing environment by passing a conda dependency file and private wheel dependency.

`environment_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted environment_args dictionary keyworded arguments](parameters.md#environment_args-dictionary-keyworded-arguments):   
A dictionary of keyword args to create a new Environment or get an existing Environment. 

### **Returns**

Environment

### **Return Type**

[Environment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.environment?view=azure-ml-py)

### **Remarks** 

Example1: Creation of new Environment with environment_type 'CondaPackageEnvironment'
 ```
 environment=create_environment(workspace=workspace,
                            environment_type='CondaPackageEnvironment',
                            environment_args={'name':<environment-name>, 
                                              'conda_packages':['scikit-learn'],
                                              'pip_wheel_files':['fedml_azure-1.0.0-py3-none-any.whl']}
                              )
 ```

 Example2: Creation of new Environment with environment_type 'CondaSpecificationEnvironment'
 ```
 environment=create_environment(workspace=workspace,
                             environment_type='CondaSpecificationEnvironment',
                             environment_args={'name':<environment-name>,
                                              'file_path':'conda_dependency.yml',
                                              'pip_wheel_files':['fedml_azure-updated_test-py3-none-any.whl']}
                              )
  
```

# **DwcAzureTrain class**

DwcAzureTrain class initializes the resources required for the model training, enables the training data to be read from SAP DWC in real time without storing it in any Azure Storage, trains a Machine Learning model and registers it. 

## **Constructor**

`DwcAzureTrain(workspace=None,workspace_args=None,experiment=None,experiment_args=None,compute_type=None,compute=None,compute_args=None,environment=None,environment_type=None,environment_args=None)`

Initializes the resources for the training such as Workspace, Environment, Compute and Experiment

### **Parameters**:

`workspace_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted workspace_args dictionary keyworded arguments](parameters.md#workspace_args-dictionary-keyworded-arguments) (optional):  
default value: None    
  A dictionary of keyword args to get an existing workspace. 

`workspace` [(azureml.core.Workspace)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py) (optional):  
default value: None      
 Assigns an existing Workspace object.    

`experiment_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted experiment_args dictionary keyworded arguments](parameters.md#experiment_args-dictionary-keyworded-arguments) (optional):    
default value: None  
A dictionary of keyword args to create a new Experiment or get an existing Experiment.

`experiment` [(azureml.core.Experiment)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py) (optional):    
 default value: None  
 Assigns an existing Experiment object.

`compute_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):    
default value: None  
Type of compute to be created. The following compute_type are supported:
 - `'AmlComputeCluster'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.AmlCompute'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)?view=azure-ml-py#:~:text=An%20Azure%20Machine%20Learning%20Compute%20(AmlCompute)%20is%20a%20managed%2D,be%20shared%20with%20other%20users.).      
 - `'AmlComputeInstance'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.ComputeInstance'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.computeinstance(class)?view=azure-ml-py).      

`compute_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted compute_args dictionary keyworded arguments](parameters.md#compute_args-dictionary-keyworded-arguments) (optional):    
default value: None  
A dictionary of keyword args to create a new Compute or get an existing Compute.

`compute` [(azureml.core.compute)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute?view=azure-ml-py) (optional):    
default value: None  
Assigns an existing Compute object. 

`environment_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):    
default value: None  
Specifies the method of creating an environment.The following environment_type are supported:
 - `'CondaPackageEnvironment'` for creating a new Environment or obtaining an existing environment by specifying pip, conda and private wheel dependency.
 - `'CondaSpecificationEnvironment'` for creating a new Environment or obtaining an existing environment by passing a conda dependency file and private wheel dependency.

`environment_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted environment_args dictionary keyworded arguments](parameters.md#environment_args-dictionary-keyworded-arguments) (optional):   
default value: None  
A dictionary of keyword args to create a new Environment or get an existing Environment. 

`environment` [(azureml.core.Environment)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.environment?view=azure-ml-py) (optional):   
default value: None  
Assigns an existing Environment object. 

### **Remarks**:

Workspace:

 - Getting an existing Workspace: Specify the 'workspace_args' parameter for getting an existing Workspace.  Example 
```
workspace_args={"subscription_id": <subscription_id>,  
                "resource_group": <resource_group>,  
                "workspace_name": <workspace_name>  
                }
```
 - Assigning an existing Workspace: Specify the 'workspace' parameter for assigning an existing Workspace.  Example
```
workspace=<workspace-object>
```

Experiment:

 - Creation of new Experiment: Specify the 'experiment_args' parameter for creating a new Experiment.  
 Example
```
  experiment_args={'name':<experiment-name>}
```
 - Getting an existing Experiment: Specify the 'experiment_args' parameter for getting an existing Experiment.  Example
```
  experiment_args={'name':<experiment-name>}
```
- Assigning an existing experiment: Specify the 'experiment'  parameter for assigning an existing Experiment.  Example
```
  experiment=<experiment-object>
```

Compute:
 - Creation of new Compute: Specify the 'compute_type' and 'compute_args' parameters for creating a new Compute.  
   Example1: Creation of a new compute with compute_type 'AmlComputeCluster'
 ```
  compute_type='AmlComputeCluster',
  compute_args={'vm_size':'Standard_D12_v2',
          'vm_priority':'lowpriority',
          'compute_name':<compute-name>,
          'min_nodes':0,
          'max_nodes':4,
          }
 ```
  Example2: Creation of a new compute with compute_type 'AmlComputeInstance'
```
  compute_type='AmlComputeInstance',
  compute_args={
      'vm_size':"Standard_D3_v2",
      'compute_name':<compute-name>
  }
```

 - Getting an existing Compute: Specify the 'compute_type' and 'compute_args' parameters for getting an existing Compute.
  Example
```
  compute_type='AmlComputeInstance',
  compute_args={
      'compute_name':<compute-name>
  }
```
 - Assigning an existing Compute: Specify the 'compute' parameter for assigning an existing Compute.  
 Example
 ```
  compute=<compute-object>
 ```

 - Note: If 'compute_type', 'compute_args' and 'compute' parameters are not specified, then no compute is used for training.

Environment:
 - Creation of new Environment: Specify the 'environment_type' and 'environment_args' parameters for creating a new Environment.  
 Example1: Creation of new Environment with environment_type 'CondaPackageEnvironment'
 ```
  environment_type='CondaPackageEnvironment',
  environment_args={'name':<environment-name>, 
                    'conda_packages':['scikit-learn'],
                    'pip_packages':['fedml_azure']
                    }
 ```

 Example2: Creation of new Environment with environment_type 'CondaSpecificationEnvironment'
 ```
  environment_type='CondaSpecificationEnvironment',
  environment_args={'name':<environment-name>,
                    'file_path':'conda_dependency.yml',
                    'pip_packages':['fedml_azure']
                    }
```
 - Getting an existing Environment: Specify the 'environment_type' and 'environment_args' parameters for getting an existing Environment.    
 Example:
 ```
  environment_type='CondaPackageEnvironment',
  environment_args={'name':<environment-name>}
 ```

 - Assigning an existing Environment: Specify the 'environment' parameter for assigning an existing Environment.  
 ```
  environment=<environment-object>
 ```


## **Methods**

[generate_run_config](#generate_run_config)                 
Copy the SAP DWC connection config file 'config.json' to 'source_directory' and generates and returns the ['azureml.core.ScriptRunConfig'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig?view=azure-ml-py) object for training.  

[submit_run](#submit_run)  
Submit an experiment with the option to download the output files and returns the active created run.  

[register_model](#register_model)  
Register a model for operationalization.

[download_files](#download_files)  
Download files from a given storage prefix (folder name) or the entire container if prefix is unspecified.

[copy_config_file](#copy_config_file)  
Copy the SAP DWC connection config file `config.json` from `config_file_path` to `script_directory`

[update_compute](#update_compute)  
Updates the compute target

[update_environment](#update_environment)  
Updates the evironment

[update_experiment](#update_experiment)  
Updates the experiment


### **generate_run_config**

Copy the SAP DWC connection config file 'config.json' to 'source_directory' and generates the ['azureml.core.ScriptRunConfig'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig?view=azure-ml-py) object for training.

`generate_run_config(config_args,is_dwc_connection_required=True,config_file_path=None)`

#### **Parameters**

`config_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted config_args dictionary keyworded arguments](parameters.md#config_args-dictionary-keyworded-arguments-for-creating-scriptrunconfig-object)     
default value: None  
A dictionary of keyword args to create a ScriptRunConfig object.

`is_dwc_connection_required` [(bool)](https://docs.python.org/3/library/functions.html#bool)    
default value: True  
When set to True, it copies the SAP DWC connection config file `config.json` from `config_file_path` to `source_directory` specified in `config_args`. This config file is used for connection to SAP DWC during the training. When SAP DWC connection is not required for the training run, set the parameter to False.

`config_file_path` [(str)](https://docs.python.org/3/library/stdtypes.html#str)   
default value: None  
The file path of the 'config.json' file which contains the connection details of SAP DWC.  

#### **Returns**

A ScriptRun

#### **Return Type**

[ScriptRun](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.script_run.scriptrun?view=azure-ml-py)

#### **Remarks**

Example 

```
src=train.generate_run_config(config_file_path='config.json',
                             config_args={
                                          'source_directory':<source_directory>,
                                          'script':<script>,
                                          'arguments':['--model_file_name', <model_file_name>,  '--table_name', <table_name>,'--table_size', <table_size>]
                                          }
                            )
```

### **submit_run**  

Submit an experiment with the option to download the output files and returns the active created run.

`submit_run(run_config,is_download=False,download_args=None,show_output=True,tags=None, **kwargs)`

#### **Parameters**

`run_config` [(object)](https://docs.python.org/3/library/functions.html#object)  
The config to be submitted.

`is_download` [(bool)](https://docs.python.org/3/library/functions.html#bool)    
default value: False  
If set to True, downloads the files from `prefix` (default is `outputs` directory of the present run) to `output_directory` (default is outputs/experiment.name/run.id).

`download_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted download_args dictionary keyworded arguments for downloading the run output](parameters.md#download_args-dictionary-keyworded-arguments-for-downloading-the-run-output)   
A dictionary of keyword args to download files from 'prefix' to 'output_directory'.

`show_output` [(bool)](https://docs.python.org/3/library/functions.html#bool)  
default value: True      
Boolean to provide more verbose output.

`tags` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None   
Tags to be added to the submitted run, {"tag": "value"}.

`kwargs` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict)  (optional)  
Additional parameters used in submit function for configurations.  

#### **Returns**

A run.

#### **Return Type**

[Run](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py)

#### **Remarks**  

Example

```
run=train.submit_run(<ScriptRunConfig-object>,is_download=True)
```

### **register_model**

Register a model for operationalization.

`register_model(run,model_args,resource_config_args=None,is_sklearn_model=False)`

#### **Parameters**

`run` [Run](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py)    
The run object to be used to register the model.

`model_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted model_args dictionary keyworded arguments to register the model](parameters.md#model_args-dictionary-keyworded-arguments-to-register-the-model)     
A dictionary of keyword args to register the model

`resource_config_args`[(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted resource_config_args for registering the model](parameters.md#resource_config_args-for-registering-the-model)     
A dictionary of keyword args to specify the resouce configuration for registering the model

`is_sklearn_model` [(bool)](https://docs.python.org/3/library/functions.html#bool)  
default value: False  
If set to True, then `'model_framework'` of `model_args` is set to [Model.Framework.SCIKITLEARN](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model.framework?view=azure-ml-py) and `'model_framework_version'` of `model_args` is set to [sklearn.\__version__\](https://scikit-learn.org/stable/) by default.

#### **Returns**

The registered model.

#### **Return type**

[Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py)

#### **Remarks**

Example
```
model=train.register_model(run=<run-object>,
                           model_args={'model_name':<model_name>,
                                       'model_path':<model_path>},
                            resource_config_args={'cpu':1, 'memory_in_gb':0.5},
                            is_sklearn_model=True
                           )

```
### **download_files**

Download files from a given storage prefix (folder name) or the entire container if prefix is unspecified.

`download_files(run,prefix='outputs', output_directory=None, output_paths=None, batch_size=100, append_prefix=True)`

#### **Parameters**

`run` [Run](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py)  
The run object used to download the files

`prefix` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default_value:'outputs'  
The filepath prefix within the container from which to download all artifacts.

`output_directory` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default_value:'outputs/experiment.name/run.id'  
An optional directory that all artifact paths use as a prefix.

`output_paths` [[str]](https://docs.python.org/3/library/stdtypes.html#list)   
Optional filepaths in which to store the downloaded artifacts. Should be unique and match length of paths.

`batch_size` [int](https://docs.python.org/3/library/functions.html#int)  
The number of files to download per batch. The default is 100 files.

`append_prefix` [bool](https://docs.python.org/3/library/functions.html#bool)   
default_value:True    
An optional flag whether to append the specified prefix from the final output file path. If False then the prefix is removed from the output file path.

### **copy_config_file**

Copy the SAP DWC connection config file `config.json` from `config_file_path` to `script_directory`

`copy_config_file(config_file_path,script_directory)`

#### **Parameters**

`config_file_path` [(str)](https://docs.python.org/3/library/stdtypes.html#str)     
The file path of the 'config.json' file which contains the connection details of SAP DWC.  

`script_directory` [(str)](https://docs.python.org/3/library/stdtypes.html#str)   
The file path of the destination.


### **update_compute**
Updates the compute target

`update_compute(compute=None,compute_args=None,compute_type=None)`

#### **Parameters**

`compute_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
default value: None
Type of compute to be created. The following compute_type are supported:
 - `'AmlComputeCluster'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.AmlCompute'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)?view=azure-ml-py#:~:text=An%20Azure%20Machine%20Learning%20Compute%20(AmlCompute)%20is%20a%20managed%2D,be%20shared%20with%20other%20users.).      
 - `'AmlComputeInstance'` for creating a new compute target or obtaining an existing compute target of type ['azureml.core.compute.ComputeInstance'](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.computeinstance(class)?view=azure-ml-py).      

`compute_args` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted compute_args dictionary keyworded arguments](parameters.md#compute_args-dictionary-keyworded-arguments) (optional):  
default value: None
A dictionary of keyword args to create a new Compute or get an existing Compute.

`compute` [(azureml.core.compute)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute?view=azure-ml-py) (optional):  
default value: None
Assigns an existing Compute object. 

### **update_environment**
Updates the environment

`update_environment(environment=None,environment_type=None,environment_args=None)`

#### **Parameters**

`environment_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):  
default value: None
Specifies the method of creating an environment.The following environment_type are supported:
 - `'CondaPackageEnvironment'` for creating a new Environment or obtaining an existing environment by specifying pip, conda and private wheel dependency.
 - `'CondaSpecificationEnvironment'` for creating a new Environment or obtaining an existing environment by passing a conda dependency file and private wheel dependency.

`environment_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted environment_args dictionary keyworded arguments](parameters.md#environment_args-dictionary-keyworded-arguments) (optional): 
default value: None
A dictionary of keyword args to create a new Environment or get an existing Environment. 

`environment` [(azureml.core.Environment)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.environment?view=azure-ml-py) (optional): 
default value: None
Assigns an existing Environment object. 


### **update_experiment**
Updates the experiment

`update_experiment(experiment=None,experiment_args=None)`

#### **Parameters**

`experiment_args` [(dict](https://docs.python.org/3/library/stdtypes.html#dict) [Accepted experiment_args dictionary keyworded arguments](parameters.md#experiment_args-dictionary-keyworded-arguments) (optional):  
default value: None
A dictionary of keyword args to create a new Experiment or get an existing Experiment.

`experiment` [(azureml.core.Experiment)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py) (optional):  
 default value: None
 Assigns an existing Experiment object.


# **Methods to deploy models and perform inferencing on the webservice endpoint**

[register_model](#register_model_for_deploy)   
Method to register a model with the provided workspace. 

[deploy](#deploy)   
Method to deploy model/models to various compute targets. 

[predict](#predict)   
Method to inference the webservice endpoints. 


### **register_model_for_deploy**

Register a model with the provided workspace.

`register_model(model_args,resource_config_args=None,is_sklearn_model=False)` 

#### **Parameters**

`model_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted model_args dictionary keyworded arguments to register the model for deployment](parameters.md#model_args-dictionary-keyworded-arguments-to-register-the-model-for-deployment)      
A dictionary of keyword args to register the model 

`resource_config_args`[(dict)]((https://docs.python.org/3/library/stdtypes.html#dict)) [Accepted resource_config_args for registering the model](parameters.md#resource_config_args-for-registering-the-model)      
A dictionary of keyword args to specify the resouce configuration for registering the model 

`is_sklearn_model` [(bool)](https://docs.python.org/3/library/functions.html#bool)   
default value: False   
If set to True, then `'model_framework'` of `model_args` is set to [Model.Framework.SCIKITLEARN](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model.framework?view=azure-ml-py) and `'model_framework_version'` of `model_args` is set to [sklearn.\__version__\](https://scikit-learn.org/stable/) by default. 

#### **Returns**

The registered model. 

#### **Return type**

[Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py)

#### **Remarks**

Example
```
from fedml_azure import register_model
model=register_model(
                     model_args={'workspace':<workspace-object>,
                                 'model_name':<model_name>,
                                 'model_path':<model_path>},
                      resource_config_args={'cpu':<cpu-cores>, 'memory_in_gb':<memory-in-gb>},
                      is_sklearn_model=True
                     )

```

## **deploy**  

Method to deploy model/models to various compute targets. 

`deploy(compute_type=None,deploy_args=None,inference_config_args=None,deploy_config_args=None)`  

Note: For deployment to Kyma Kubernetes the following steps needs to be completed:

- Create a Service Principal as follows:

  - [(Register an application with Azure AD and create a service principal)](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal)  

  - Get the Application (client) ID by referring [(get application id)](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#get-tenant-and-app-id-values-for-signing-in). The Application (client) ID is the "SERVICE_PRINCIPAL_ID".  

  - Create a new application secret by referring [(create new application secret)](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#option-2-create-a-new-application-secret). The value of the client secret displayed is the "SERVICE_PRINCIPAL_PASSWORD".  

  - Store the "SERVICE_PRINCIPAL_ID" and "SERVICE_PRINCIPAL_PASSWORD" in a json file (example: sp_config.json) and provide the file path to `deploy_args['sp_config_path']`. Refer [(deploy_args)](parameters.md#deploy_args-dictionary-keyworded-arguments-to-deploy-the-model-to-kyma) parameters for kyma below for more details.  

- Create a Kyma service account and create a kubeconfig.yaml file to connect to Kyma Kubernetes

  - Create a Kyma service account by referring the [(tutorial)](https://developers.sap.com/tutorials/kyma-create-service-account.html#55c9eee0-eaee-4005-a6a3-4b72f83fe186).    

  - In step 2.1 of the [(tutorial)](https://developers.sap.com/tutorials/kyma-create-service-account.html#55c9eee0-eaee-4005-a6a3-4b72f83fe186), add the following fields:    

    - Add 'namespaces' under 'rules -> resources' section of yaml file.  
    - Add 'watch' under 'rules -> verbs' section of yaml file.  

  - In step 4.1 of the [(tutorial)](https://developers.sap.com/tutorials/kyma-create-service-account.html#55c9eee0-eaee-4005-a6a3-4b72f83fe186), replace the following:  

    - Replace the value of 'name' under 'clusters' section with the cluster name of the kyma kubernetes cluster.
    - Replace the value of 'name' under 'users' section and 'user' under 'contexts'-> 'context' with 'OIDCUser' user.
    - Replace the value of 'name', 'context -> cluster' under 'contexts' section with the cluster name of the kyma kubernetes cluster.
    - Replace the value of 'current-context' with the cluster name of the kyma kubernetes cluster.

  - Provide the generated  'kubeconfig.yaml' file path to `deploy_args['kubeconfig_path']` to connect to Kyma Kubernetes. Refer [(deploy_args)](parameters.md#deploy_args-dictionary-keyworded-arguments-to-deploy-the-model-to-kyma) parameters for kyma below for more details.

### **Parameters**:


`compute_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str) (optional):   
Type of compute to deploy the webservice to. The supported compute_type are 'ACI', 'AKS', 'Local' and 'Kyma': 

- `ACI`: Deploys the model/models as a webservice endpoint to Azure Container Instances.  
- `AKS`: Deploys the model/models as a webservice endpoint to Azure Kubernetes Service.  
- `Local`: Deploys the model/models as a webservice endpoint locally.  
- `Kyma` : Deploys the model/models as a webservice endpoint to kyma kubernetes.


`deploy_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict))      
A dictionary of keyword args to deploy the model. 

- `deploy_config_args` for `ACI`,`AKS` and `Local` [Accepted deploy_args dictionary keyworded arguments to deploy the model](parameters.md#deploy_args-dictionary-keyworded-arguments-to-deploy-the-model) 
- `deploy_config_args` for `Kyma` [Accepted deploy_args dictionary keyworded arguments to deploy the model to kyma](parameters.md#deploy_args-dictionary-keyworded-arguments-to-deploy-the-model-to-kyma) 

`inference_config_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict))    
A dictionary of keyword args to determine required model properties. 

- `inference_config_args` for `ACI`,`AKS` and `Local` [Accepted inference_config_args dictionary keyworded arguments to determine required model properties](parameters.md#inference_config_args-dictionary-keyworded-arguments-to-determine-required-model-properties)    
- `inference_config_args` for `Kyma` [Accepted inference_config_args dictionary keyworded to determine required model properties for kyma](parameters.md#inference_config_args-dictionary-keyworded-arguments-to-determine-required-model-properties-for-kyma) 

`deploy_config_args` [(dict)]((https://docs.python.org/3/library/stdtypes.html#dict))  
Note: This needs to passed only if the `compute_type` is `ACI`,`AKS` and `Local`. It is not required in case the `compute_type` is `Kyma`.
A dictionary of keyword args to configure the webservice.

The accepted `deploy_config_args` for the compute types are as follows: 

- `deploy_config_args` for ACI [Accepted ACI deploy_config_args dictionary keyworded arguments to configure the webservice](parameters.md#aci-deploy_config_args-dictionary-keyworded-arguments-to-configure-the-webservice)      
A dictionary of keyword args to deploy the model. 

- `deploy_config_args` for AKS [Accepted AKS deploy_config_args dictionary keyworded arguments to configure the webservice](parameters.md#aks-deploy_config_args-dictionary-keyworded-arguments-to-configure-the-webservice)      
A dictionary of keyword args to deploy the model. 

- `deploy_config_args` for Local [Accepted Local deploy_config_args dictionary keyworded arguments to configure the webservice](parameters.md#local-deploy_config_args-dictionary-keyworded-arguments-to-configure-the-webservice)      
A dictionary of keyword args to deploy the model. 


### **Returns**

For compute types `ACI`,`AKS` and `Local`: 

`endpoint_url,api_key,service` 

Note The `api_key` is only returned if the compute_type is `AKS`. 

For compute_type `'Kyma'` 

`endpoint_url`

### **Return Type**

`endpoint_url` [str](https://docs.python.org/3/library/stdtypes.html#str)  

`api_key` [str](https://docs.python.org/3/library/stdtypes.html#str)  

`service` [Webservice](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice(class)?view=azure-ml-py) 

### **Remarks**

Example 1: Deploy a model locally 

```
from fedml_azure import deploy
local_endpoint,_,local_service=deploy(compute_type='local',
                inference_config_args={'entry_script':<entry-script-path>, 'environment':<environment-object>},
                deploy_config_args={'port':<port>},
                deploy_args={'workspace':<workspace-object>,'name':<service-name>,'models':<list-of-models>}
                )
```

Example 2: Deploy a model to ACI 

```
from fedml_azure import deploy
aci_endpoint,_,aci_service=deploy(compute_type='ACI',
                inference_config_args={'entry_script':<entry-script-path>, 'environment':<environment-object>},
                deploy_config_args={'cpu_cores':<no-of-cpu-cores>, 'memory_gb':<memory-in-gb>},
                deploy_args={'workspace':<workspace-object>,'name':<service-name>,'models':<list-of-models>}
                )
```

Example 3: Deploy a model to AKS 

```
from fedml_azure import deploy
aks_endpoint,api_key,aks_service=deploy(compute_type='AKS',
                inference_config_args={'entry_script':<entry-script-path>, 'environment':<environment-object>},
                deploy_args={'workspace':<workspace-object>,'name':<service-name>,'models':<list-of-models>,'deployment_target':<aks-compute-object>}
                )
```


Example 4: Deploy a model to Kyma Kubernetes 

```
from fedml_azure import deploy
kyma_endpoint=deploy(compute_type='Kyma',
                    inference_config_args={'entry_script':<entry-script-path>, 'environment':<environment-object>},
                    deploy_args={'workspace':<workspace-object>,
                                'name':<service-name>,
                                'models':<list-of-models>,
                                'num_replicas':<num-replicas>,
                                'kubeconfig_path':<path-to-kubeconfig.yaml>,
                                'sp_config_path':<path-to-sp_config.json>
                                })
```

## **predict**`

Method to inference the webservice endpoints. 

`predict(data,compute_type=None,api_key=None,service=None,endpoint_url=None)` 

### **Parameters**

`endpoint_url` [(str)](https://docs.python.org/3/library/stdtypes.html#str):    
The endpoint url used for inferencing the webserice endpoint. 

`compute_type` [(str)](https://docs.python.org/3/library/stdtypes.html#str):    
The compute_type where the webservice is deployed. The supported compute types are as follows: 

- `ACI`: Webservice Endpoint in Azure Container Instances.  
- `AKS`: Webservice Endpoint in Azure Kubernetes Service.  
- `Local`: Webservice Endpoint present locally.  
- `Kyma`: Webservice Endpoint in Kyma Kubernetes.

`data` (Serialized json object):   
Required 
The data used for inferencing. 

`api_key` [(str)](https://docs.python.org/3/library/stdtypes.html#str):     
Required   
The api_key obtained from the [deploy](#deploy) method. The `api_key` is only returned if the compute_type is `AKS`.   

`service` [(Webservice)](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice?view=azure-ml-py).  
The Webservice object to be used to invoke the endpoint. Note the Webservice object types include the following:   

- [AksWebservice](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.akswebservice?view=azure-ml-py)  
- [AciWebservice](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice?view=azure-ml-py)  
- [LocalWebservice](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.localwebservice?view=azure-ml-py) 


Note:

There are two ways to inference the data using `predict` function:

- By using the endpoint_url as follows:

  `predict(endpoint_url=<endpoint-url>,compute_type=<compute-type>,data=<test-data>)`

- By using the Webservice object as follows:

  `predict(service=<Webservice-object>,data=<test-data>)`


### **Returns**

The result of inferencing.

### **Remarks**

Example 1: Inferencing ACI webservice endpoint 
```
data = json.dumps({
    'data': <pandas-dataframe-containing-inferencing-data>.values.tolist()
})

# Option 1: Predict using the endpoint_url

from fedml_azure import predict
predict(endpoint_url=<aci-endpoint-url>,data=<inferencing-data>,compute_type='ACI')

# Option 2: Predict using the Webservice object

predict(service=<aci-webservice>,data=<test-data>)
```

Example 2: Inferencing AKS webservice endpoint 
```
data = json.dumps({
    'data': <pandas-dataframe-containing-inferencing-data>.values.tolist()
})

# Option 1: Predict using the endpoint_url

from fedml_azure import predict
predict(endpoint_url=<aks-endpoint-url>,data=<inferencing-data>,compute_type='AKS')

# Option 2: Predict using the Webservice object

predict(service=<aks-webservice>,data=<test-data>)
```

Example 3: Inferencing Local webservice endpoint 
```
data = json.dumps({
    'data': <pandas-dataframe-containing-inferencing-data>.values.tolist()
})

# Option 1: Predict using the endpoint_url

from fedml_azure import predict
predict(endpoint_url=<local-endpoint-url>,data=<inferencing-data>,compute_type='Local')

# Option 2: Predict using the Webservice object

predict(service=<local-webservice>,data=<test-data>)
```

Example 4: Inferencing Kyma webservice endpoint 
```
data = json.dumps({
    'data': <pandas-dataframe-containing-inferencing-data>.values.tolist()
})

# Predict using the endpoint_url

from fedml_azure import predict
predict(endpoint_url=<kyma-endpoint-url>,data=<inferencing-data>,compute_type='Kyma')
```

