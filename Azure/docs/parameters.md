# **workspace_args dictionary keyworded arguments**

The following are the dictionary keys accepted in the parameter 'workspace_args':

`'subscription_id'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
The Azure subscription ID containing the workspace.    

`'resource_group'` [str](https://docs.python.org/3/library/stdtypes.html#str)            
The resource group containing the workspace.   

`'workspace_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)            
The existing workspace name.   

`'auth'` [ServicePrincipalAuthentication](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.authentication.serviceprincipalauthentication?view=azure-ml-py) or [InteractiveLoginAuthentication](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.authentication.interactiveloginauthentication?view=azure-ml-py) or [MsiAuthentication](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.authentication.msiauthentication?view=azure-ml-py)    
The authentication object. For more details, see [https://aka.ms/aml-notebook-auth](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/manage-azureml-service/authentication-in-azureml/authentication-in-azureml.ipynb). If None, the default Azure CLI credentials will be used or the API will prompt for credentials.   

`'_location'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
Internal use only.   

`'_disable_service_check'` [bool](https://docs.python.org/3/library/functions.html#bool)    
Internal use only.  

`'_workspace_id'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
Internal use only.   

`'sku'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value:'basic'         
The parameter is present for backwards compatibility and is ignored. For more information see [Azure Machine Learning SKUs](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning#sku).  

`'_cloud'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value:'AzureCloud'       
Internal use only.  

# **experiment_args dictionary keyworded arguments**

The following are the dictionary keys accepted in the parameter 'experiment_args':  

`'name'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
The experiment name.  

`'kwargs'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)  
A dictionary of keyword args.  


# **compute_args dictionary keyworded arguments**

# **compute_args dictionary keyworded arguments for compute_type 'AmlComputeCluster'**

The following are the dictionary keys accepted in the parameter 'compute_args' for compute_type 'AmlComputeCluster':

`'compute_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
The name of the AmlCompute object to create/retrieve.      

`'vm_size'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
The size of agent VMs. More details can be found here: [https://aka.ms/azureml-vm-details](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target#supported-vm-series-and-sizes). Note that not all sizes are available in all regions, as detailed in the previous link. If not specified, defaults to Standard_NC6.  

`'vm_priority'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: dedicated    
The VM priority, dedicated or lowpriority.  

`'min_nodes'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: 0    
The minimum number of nodes to use on the cluster. If not specified, defaults to 0.  

`'max_nodes'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: None    
The maximum number of nodes to use on the cluster. If not specified, defaults to 4.  

`'idle_seconds_before_scaledown'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: 1800      
Node idle time in seconds before scaling down the cluster. If not specified, defaults to 1800.

`'admin_username'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None    
The name of the administrator user account which can be used to SSH into nodes.

`'admin_user_password'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
The password of the administrator user account.

`'admin_user_ssh_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
The SSH public key of the administrator user account.

`'vnet_resourcegroup_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
The name of the resource group where the virtual network is located.

`'vnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
The name of the virtual network.

`'subnet_name'`[str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
The name of the subnet inside the VNet.

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)  
default value: None  
A dictionary of key value tags to provide to the compute object.

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
A description to provide to the compute object.

`'remote_login_port_public_access'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: NotSpecified  

State of the public SSH port. Possible values are:
 - Disabled - Indicates that the public ssh port is closed on all nodes of the cluster.
 - Enabled - Indicates that the public ssh port is open on all nodes of the cluster.
 - NotSpecified - Indicates that the public ssh port is closed on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be this default value only during cluster creation time. After creation, it will be either enabled or disabled.

`'identity_type'` [string](https://docs.python.org/3/library/string.html#module-string)  
default value: None      
Possible values are:  
- SystemAssigned - System assigned identity
- UserAssigned - User assigned identity. Requires identity id to be set.

`'identity_id'` [list](https://docs.python.org/3/library/stdtypes.html#list)  
default value: None  
List of resource ids for the user assigned identity.

`'location'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None  
Location to provision cluster in.

`'show_output'` [bool](https://docs.python.org/3/library/functions.html#bool)  
default value: True      
Boolean to provide more verbose output.

`'min_node_count'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None  
Minimum number of nodes to wait for before considering provisioning to be complete. This doesn't have to equal the minimum number of nodes that the compute was provisioned with, however it should not be greater than that.  

`'timeout_in_minutes'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: 20  
The duration in minutes to wait before considering provisioning to have failed.  

 # **compute_args dictionary keyworded arguments for compute_type 'AmlComputeInstance'**

The following are the dictionary keys accepted in the parameter 'compute_args' for compute_type 'AmlComputeInstance':

 `'compute_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)       
The name of the ComputeInstance object to create/retrieve.    

`'vm_size'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
The size of agent VMs. More details can be found here: [https://aka.ms/azureml-vm-details](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target#supported-vm-series-and-sizes). Note that not all sizes are available in all regions, as detailed in the previous link. Defaults to Standard_NC6.  
 
`'ssh_public_access'` [bool](https://docs.python.org/3/library/functions.html#bool)      
default value: False    
Indicates the state of the public SSH port. Possible values are:  

 - False - The public SSH port is closed.
 - True - The public SSH port is open.

`'admin_user_ssh_public_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None  
The SSH public key of the administrator user account.  

`'vnet_resourcegroup_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None  
The name of the resource group where the virtual network is located.  

`'vnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None  
The name of the virtual network.  

`'subnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
default value: None  
The name of the subnet inside the vnet.

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)    
default value: None  
An optional dictionary of key value tags to associate with the compute object.  

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
default value: None  
An optional description for the compute object.  

`'assigned_user_object_id'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
default value: None  
The AAD Object ID of the assigned user (preview).  

`'assigned_user_tenant_id'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None    
The AAD Tenant ID of the assigned user (preview).  

`'show_output'` [bool](https://docs.python.org/3/library/functions.html#bool)  
default value: True      
Boolean to provide more verbose output.  

# **environment_args dictionary keyworded arguments**

# **environment_args dictionary keyworded arguments for environment_type 'CondaPackageEnvironment'**

The following are the dictionary keys accepted in the parameter 'environment_args' for compute_type 'CondaPackageEnvironment':

`'name'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
The name of the environment.  

`'pip_indexurl'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None
The pip index URL. If not specified, the SDK origin index URL will be used.

`'pip_packages'` [list[str]](https://docs.python.org/3/library/stdtypes.html#list)  
default value: ["azureml-defaults", "pandas"]  
A list of pip packages.

`'conda_packages'` [list[str]](https://docs.python.org/3/library/stdtypes.html#list)  
default value: ["pip"]  
A list of conda packages.

`'python_version'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: 3.6.2  
The Python version.

`'pin_sdk_version'` [bool](https://docs.python.org/3/library/functions.html#bool)  
default value: True  
Indicates whether to pin SDK packages to the client version.

`'pip_wheel_files'` [list[str]](https://docs.python.org/3/library/stdtypes.html#list)  
default value: None  
A list of paths to the local pip wheel on disk, including the file extension.

# **environment_args dictionary keyworded arguments for environment_type 'CondaSpecificationEnvironment'**

The following are the dictionary keys accepted in the parameter 'environment_args' for compute_type 'CondaSpecificationEnvironment':

`'name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
The environment name.

`'file_path'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
The conda environment specification YAML file path.  

`'pip_wheel_files'` [list[str]](https://docs.python.org/3/library/stdtypes.html#list)  
default value: None    
A list of paths to the local pip wheel on disk, including the file extension.


# **config_args dictionary keyworded arguments for creating ScriptRunConfig object**

`'source_directory'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
A local directory containing code files needed for a run.

`'script'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
The file path relative to the source_directory of the script to be run.

`'arguments'` [list](https://docs.python.org/3/library/stdtypes.html#list) or [str](https://docs.python.org/3/library/stdtypes.html#str)  
Optional command line arguments to pass to the training script. Arguments are passed in pairs, for example, ['--arg1', arg1_val, '--arg2', arg2_val].

`'run_config'` [RunConfiguration](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.runconfig.runconfiguration?view=azure-ml-py)  
Optional run configuration to use.

`'_telemetry_values'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)  
Internal use only.

`'distributed_job_config'` <xref:azureml.core.runconfig.TensorflowConfiguration,azureml.core.runconfig.MpiConfiguration> or [PyTorchConfiguration](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.runconfig.pytorchconfiguration?view=azure-ml-pyhttps://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.runconfig.pytorchconfiguration?view=azure-ml-py)
For jobs that require additional distributed job-specific configurations.

`'resume_from'` [DataPath](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.datapath.datapath?view=azure-ml-py)  
The DataPath containing the checkpoint or model files from which to resume the experiment.

`'max_run_duration_seconds'`[int](https://docs.python.org/3/library/functions.html#int)  
The maximum time allowed for the run. The system will attempt to automatically cancel the run if it took longer than this value.

`'command'` [list](https://docs.python.org/3/library/stdtypes.html#list) or [str](https://docs.python.org/3/library/stdtypes.html#str)  
The command to be submitted for the run. The command property can also be used instead of script/arguments. Both command and script/argument properties cannot be used together to submit a run. To submit a script file using the command property - ['python', 'train.py', '--arg1', arg1_val] To run an actual command - ['ls']

`'docker_runtime_config'` [DockerConfiguration](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.runconfig.dockerconfiguration?view=azure-ml-py)  
For jobs that require Docker runtime-specific configurations.

# **download_args dictionary keyworded arguments for downloading the run output**

`'prefix'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default_value:'outputs'  
The filepath prefix within the container from which to download all artifacts.

`'output_directory'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default_value:'outputs/experiment.name/run.id'  
An optional directory that all artifact paths use as a prefix.

`'output_paths'` [[str]](https://docs.python.org/3/library/stdtypes.html#list)   
Optional filepaths in which to store the downloaded artifacts. Should be unique and match length of paths.

`'batch_size'` [int](https://docs.python.org/3/library/functions.html#int)  
The number of files to download per batch. The default is 100 files.

`'append_prefix'` [bool](https://docs.python.org/3/library/functions.html#bool)   
default_value:True    
An optional flag whether to append the specified prefix from the final output file path. If False then the prefix is removed from the output file path.



# **model_args dictionary keyworded arguments to register the model**

`'model_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
The name of the model.

`'model_path'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None  
The relative cloud path to the model, for example, "outputs/modelname". When not specified (None), model_name is used as the path.

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)  
default value: None  
A dictionary of key value tags to assign to the model.

`'properties'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)    
default value: None    
A dictionary of key value properties to assign to the model. These properties cannot be changed after model creation, however new key value pairs can be added.

`'model_framework'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default_value: [Model.Framework.SCIKITLEARN](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model.framework?view=azure-ml-py) if `is_sklearn_model` is set to 'True' else None.  
The framework of the model to register. Currently supported frameworks: TensorFlow, ScikitLearn, Onnx, Custom, Multi

`'model_framework_version'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: [(sklearn.\__version__\)](https://scikit-learn.org/stable/) if `is_sklearn_model` is set to 'True' else None    
The framework version of the registered model.

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
default value: None  
An optional description of the model.

`'datasets'` [list](https://docs.python.org/3/library/stdtypes.html#list)  
default value: None  
A list of tuples where the first element describes the dataset-model relationship and the second element is the dataset.

`'sample_input_dataset'` [AbstractDataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.abstract_dataset.abstractdataset?view=azure-ml-py)  
default value: None  
Optional. Sample input dataset for the registered model

`'sample_output_dataset'` [AbstractDataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.abstract_dataset.abstractdataset?view=azure-ml-py)  
default value: None  
Optional. Sample output dataset for the registered model

`kwargs` [dict](https://docs.python.org/3/library/stdtypes.html#dict)  
Optional parameters.

## **resource_config_args for registering the model**

`'cpu'` [float](https://docs.python.org/3/library/functions.html#float)    
The number of CPU cores to allocate for this resource. Can be a decimal.

`'memory_in_gb'` [float](https://docs.python.org/3/library/functions.html#float)    
The amount of memory (in GB) to allocate for this resource. Can be a decimal.

`'gpu'` [int](https://docs.python.org/3/library/functions.html#int)    
The number of GPUs to allocate for this resource.





