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
                                              'pip_wheel_files':['fedml_azure-1.0.0-py3-none-any.whl']}
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

 - Getting an existing Workspace: Specify the 'workspace_args' parameter for getting an existing Workspace.  
 Example 
```
workspace_args={"subscription_id": <subscription_id>,  
                "resource_group": <resource_group>,  
                "workspace_name": <workspace_name>  
                }
```
 - Assigning an existing Workspace: Specify the 'workspace' parameter for assigning an existing Workspace.  
 Example
```
workspace=<workspace-object>
```

Experiment:

 - Creation of new Experiment: Specify the 'experiment_args' parameter for creating a new Experiment.  
 Example
```
  experiment_args={'name':<experiment-name>}
```
 - Getting an existing Experiment: Specify the 'experiment_args' parameter for getting an existing Experiment.  
 Example
```
  experiment_args={'name':<experiment-name>}
```
- Assigning an existing experiment: Specify the 'experiment'  parameter for assigning an existing Experiment.  
Example
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
                    'pip_wheel_files':['fedml_azure-1.0.0-py3-none-any.whl']}
 ```

 Example2: Creation of new Environment with environment_type 'CondaSpecificationEnvironment'
 ```
  environment_type='CondaSpecificationEnvironment',
  environment_args={'name':<environment-name>,
                    'file_path':'conda_dependency.yml',
                    'pip_wheel_files':['fedml_azure-updated_test-py3-none-any.whl']}
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
If set to True, then `'model_framework'` of `model_args` is set to [Model.Framework.SCIKITLEARN](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model.framework?view=azure-ml-py) and `'model_framework_version'` of `model_args` is set to [(sklearn.\__version__\)](https://scikit-learn.org/stable/) by default.

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


