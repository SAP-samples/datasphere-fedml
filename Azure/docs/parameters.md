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

# **compute_args dictionary keyworded arguments for compute_type 'AKS'**

The following are the dictionary keys accepted in the parameter 'compute_args' for compute_type 'AKS':

`'agent_count'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: None         
The number of agents (VMs) to host containers. Defaults to 3.      

`'vm_size'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None       
The size of agent VMs. A full list of options can be found here: [(https://aka.ms/azureml-aks-details)](https://aka.ms/azureml-aks-details). Defaults to Standard_D3_v2.   
 
`'ssl_cname'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None       
A CName to use if enabling SSL validation on the cluster. Must provide all three CName, cert file, and key file to enable SSL validation.   

`'ssl_cert_pem_file'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None    
A file path to a file containing cert information for SSL validation. Must provide all three CName, cert file, and key file to enable SSL validation.  

`'ssl_key_pem_file'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None    
A file path to a file containing key information for SSL validation. Must provide all three CName, cert file, and key file to enable SSL validation.   

`'location'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None    
The location to provision cluster in. If not specified, will default to workspace location. Available regions for this compute can be found here: [(https://azure.microsoft.com/global-infrastructure/services/?regions=all&products=kubernetes-service)](https://azure.microsoft.com/global-infrastructure/services/?regions=all&products=kubernetes-service)   

`'vnet_resourcegroup_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
default value: None    
The name of the resource group where the virtual network is located.   

`'vnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)         
default value: None    
The name of the virtual network.    

`'subnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
default value: None    
The name of the subnet inside the vnet.    

`'service_cidr'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
default value: None    
A CIDR notation IP range from which to assign service cluster IPs.   

`'dns_service_ip'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None      
Containers DNS server IP address.    

`'docker_bridge_cidr'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None         
A CIDR notation IP for Docker bridge.     

`'cluster_purpose'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None         
Targeted usage of the cluster. This is used to provision Azure Machine Learning components to ensure the desired level of fault-tolerance and QoS. AksCompute.ClusterPurpose class is provided for convenience of specifying available values. More detailed information of these values and their use cases can be found here: [(https://aka.ms/azureml-create-attach-aks)](https://aka.ms/azureml-create-attach-aks)   

`'load_balancer_type'` [str](https://docs.python.org/3/library/stdtypes.html#str)        
default value: None           
Load balancer type of AKS cluster. Valid values are PublicIp and InternalLoadBalancer. Default value is PublicIp.     

`'load_balancer_subnet'` [str](https://docs.python.org/3/library/stdtypes.html#str)      
default value: None         
Load balancer subnet of AKS cluster. It can be used only when Internal Load Balancer is used as load balancer type. Default value is aks-subnet.  

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
default value: [sklearn.\__version__\](https://scikit-learn.org/stable/) if `is_sklearn_model` is set to 'True' else None    
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

# **model_args dictionary keyworded arguments to register the model for deployment**

`'workspace'` [Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace(class)?view=azure-ml-py)  
Required  
The workspace to register the model with. 

`'model_path'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required      
The path on the local file system where the model assets are located. This can be a direct pointer to a single file or folder. If pointing to a folder, the child_paths parameter can be used to specify individual files to bundle together as the Model object, as opposed to using the entire contents of the folder.

`'model_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required    
The name to register the model with. 

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None   
An optional dictionary of key value tags to assign to the model. 

`'properties'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)     
default value: None     
An optional dictionary of key value properties to assign to the model. These properties can't be changed after model creation, however new key value pairs can be added.

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: None   
A text description of the model. 

`'datasets'` [list](https://docs.python.org/3/library/stdtypes.html#list)   
default value: None   
A list of tuples where the first element describes the dataset-model relationship and the second element is the dataset. 

`'model_framework'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
default_value: [Model.Framework.SCIKITLEARN](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model.framework?view=azure-ml-py) if `is_sklearn_model` is set to 'True' else None.   
The framework of the registered model. Using the system-supported constants from the Framework class allows for simplified deployment for some popular frameworks. 

`'model_framework_version'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
default value: [sklearn.\__version__\](https://scikit-learn.org/stable/) if `is_sklearn_model` is set to 'True' else None    
The framework version of the registered model. 

`'child_paths'` [list](https://docs.python.org/3/library/stdtypes.html#list)  
default value: None      
If provided in conjunction with a model_path to a folder, only the specified files will be bundled into the Model object. 

`'sample_input_dataset'` [AbstractDataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.abstract_dataset.abstractdataset?view=azure-ml-py)   
default value: None   
Optional. Sample input dataset for the registered model 

`'sample_output_dataset'` [AbstractDataset](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.abstract_dataset.abstractdataset?view=azure-ml-py)   
default value: None   
Optional. Sample output dataset for the registered model 


# **deploy_args dictionary keyworded arguments to deploy the model**

`'workspace'` [Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace(class)?view=azure-ml-py)  
Required  
A Workspace object to associate the Webservice with. 

`'name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required     
The name to give the deployed service. Must be unique to the workspace, only consist of lowercase letters, numbers, or dashes, start with a letter, and be between 3 and 32 characters long. 

`'models'` [list](https://docs.python.org/3/library/stdtypes.html#list)  
Required     
A list of model objects. 

`'overwrite'` [bool](https://docs.python.org/3/library/functions.html#bool)     
default value: False  
Indicates whether to overwrite the existing service if a service with the specified name already exists. 

`'show_output'` [bool](https://docs.python.org/3/library/functions.html#bool)      
default value: False  
Indicates whether to display the progress of service deployment. 

# **deploy_args dictionary keyworded arguments to deploy the model to kyma**

`'workspace'` [Workspace](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace(class)?view=azure-ml-py)  
Required  
A Workspace object to associate the Webservice with. 

`'name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required     
The name to give the deployed service. Must be unique to the workspace, only consist of lowercase letters, numbers, or dashes, start with a letter, and be between 3 and 32 characters long. 

`'models'` [list](https://docs.python.org/3/library/stdtypes.html#list)  
Required     
A list of model objects. 

`'overwrite_service'` [bool](https://docs.python.org/3/library/functions.html#bool)     
default value: False  
Indicates whether to overwrite the existing service and deployment if a service with the specified name already exists. 

`'kubeconfig_path'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required     
The file path to 'kubeconfig.yaml' file. This file is required to connect to Kyma Kubernetes.

`'sp_config_path'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required     
The file path to 'sp_config.json' file. This file must contain the Service Principal credentials.

### **Remarks**
Example: The contents of the 'sp_config.json' must follow the following format:

```
{
    "SERVICE_PRINCIPAL_ID":<SERVICE_PRINCIPAL_ID>,
    "SERVICE_PRINCIPAL_PASSWORD":<SERVICE_PRINCIPAL_PASSWORD>
}
```
`'num_replicas'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: 1 
The number of pods to allocate for this Webservice.



# **inference_config_args dictionary keyworded arguments to determine required model properties**

`'entry_script'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required  
The path to a local file that contains the code to run for the image. 

`'runtime'` [str](https://docs.python.org/3/library/stdtypes.html#str)       
The runtime to use for the image. Current supported runtimes are 'spark-py' and 'python'. 

`'conda_file'` [str](https://docs.python.org/3/library/stdtypes.html#str)     
The path to a local file containing a conda environment definition to use for the image. 

`'extra_docker_file_steps'` [str](https://docs.python.org/3/library/stdtypes.html#str)   
The path to a local file containing additional Docker steps to run when setting up image. 

`'source_directory'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
Required  
The path to the folder that contains all files to create the image. 

`'enable_gpu'` [bool](https://docs.python.org/3/library/functions.html#bool)     
Indicates whether to enable GPU support in the image. The GPU image must be used on Microsoft Azure Services such as Azure Container Instances, Azure Machine Learning Compute, Azure Virtual Machines, and Azure Kubernetes Service. Defaults to False. 

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
A description to give this image. 

`'base_image'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
A custom image to be used as base image. If no base image is given then the base image will be used based off of given runtime parameter.  

`'base_image_registry'` [ContainerRegistry](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.container_registry.containerregistry?view=azure-ml-py)     
The image registry that contains the base image. 

`'cuda_version'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
The Version of CUDA to install for images that need GPU support. The GPU image must be used on Microsoft Azure Services such as Azure Container Instances, Azure Machine Learning Compute, Azure Virtual Machines, and Azure Kubernetes Service. Supported versions are 9.0, 9.1, and 10.0. If enable_gpu is set, this defaults to '9.1'. 

`'environment'` [Environment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment(class)?view=azure-ml-py)    
Required   
An environment object to use for the deployment. The environment doesn't have to be registered.


# **inference_config_args dictionary keyworded arguments to determine required model properties for kyma**

`'entry_script'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
Required  
The path to a local file that contains the code to run for the image. 

`'source_directory'` [str](https://docs.python.org/3/library/stdtypes.html#str)    
Required  
The path to the folder that contains all files to create the image.  
Note: If `'source_directory'` is provided then the path of the parameter `'entry_script'` must be relative to the `'source_directory'`.

`'environment'` [Environment](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment(class)?view=azure-ml-py)    
Required   
An environment object to use for the deployment. The environment doesn't have to be registered.

# **aci deploy_config_args dictionary keyworded arguments to configure the webservice**

`'cpu_cores'` [float](https://docs.python.org/3/library/functions.html#float)    
default value: None  
The number of CPU cores to allocate for this Webservice. Can be a decimal. Defaults to 0.1 

`'memory_gb'` [float](https://docs.python.org/3/library/functions.html#float)   
default value: None       
The amount of memory (in GB) to allocate for this Webservice. Can be a decimal. Defaults to 0.5 

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None   
A dictionary of key value tags to give this Webservice. 

`'properties'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None  
A dictionary of key value properties to give this Webservice. These properties cannot be changed after deployment, however new key value pairs can be added. 

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
A description to give this Webservice. 

`'location'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
The Azure region to deploy this Webservice to. If not specified the Workspace location will be used. For more details on available regions, see [Products by region](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=container-instances). 

`'auth_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)     
default value: None  
Whether or not to enable auth for this Webservice. Defaults to False. 

`'ssl_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)    
default value: None     
Whether or not to enable SSL for this Webservice. Defaults to False. 

`'enable_app_insights'` [bool](https://docs.python.org/3/library/functions.html#bool)   
default value: None    
Whether or not to enable AppInsights for this Webservice. Defaults to False. 

`'ssl_cert_pem_file'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None     
The cert file needed if SSL is enabled. 

`'ssl_key_pem_file'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
The key file needed if SSL is enabled. 

`'ssl_cname'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
The cname for if SSL is enabled. 

`'dns_name_label'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
The DNS name label for the scoring endpoint. If not specified a unique DNS name label will be generated for the scoring endpoint. 

`'primary_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
A primary auth key to use for this Webservice. 

`'secondary_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
A secondary auth key to use for this Webservice. 

`'collect_model_data'` [bool](https://docs.python.org/3/library/functions.html#bool)   
default value: None   
Whether or not to enabled model data collection for the Webservice. 

`'cmk_vault_base_url'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
customer managed key vault base url 

`'cmk_key_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
customer managed key name. 

`'cmk_key_version'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
customer managed key version. 

`'vnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None       
virtual network name. 

`'subnet_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None     
subnet name within virtual network. 


# **aks deploy_config_args dictionary keyworded arguments to configure the webservice**

`'autoscale_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)      
default value: None  
Whether or not to enable autoscaling for this Webservice. Defaults to True if num_replicas is None. 

`'autoscale_min_replicas'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: None        
The minimum number of containers to use when autoscaling this Webservice. Defaults to 1. 

`'autoscale_max_replicas'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: None    
The maximum number of containers to use when autoscaling this Webservice. Defaults to 10. 

`'autoscale_refresh_seconds'` [int](https://docs.python.org/3/library/functions.html#int)   
default value: None  
How often the autoscaler should attempt to scale this Webservice. Defaults to 1. 

`'autoscale_target_utilization'` [int](https://docs.python.org/3/library/functions.html#int)    
default value: None       
The target utilization (in percent out of 100) the autoscaler should attempt to maintain for this Webservice. Defaults to 70. 

`'collect_model_data'` [bool](https://docs.python.org/3/library/functions.html#bool)   
default value: None      
Whether or not to enable model data collection for this Webservice. Defaults to False. 

`'auth_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)      
default value: None  
Whether or not to enable auth for this Webservice. Defaults to False. 

`'cpu_cores'` [float](https://docs.python.org/3/library/functions.html#float)  
default value: None     
The number of cpu cores to allocate for this Webservice. Can be a decimal. Defaults to 0.1. Corresponds to the pod core request, not the limit, in Azure Kubernetes Service. 

`'memory_gb'` [float](https://docs.python.org/3/library/functions.html#float)   
default value: None     
The amount of memory (in GB) to allocate for this Webservice. Can be a decimal. Defaults to 0.5. Corresponds to the pod memory request, not the limit, in Azure Kubernetes Service. 

`'enable_app_insights'` [bool](https://docs.python.org/3/library/functions.html#bool)  
default value: None     
Whether or not to enable Application Insights logging for this Webservice. Defaults to False. 

`'scoring_timeout_ms'` [int](https://docs.python.org/3/library/functions.html#int)   
default value: None      
A timeout to enforce for scoring calls to this Webservice. Defaults to 60000. 

`'replica_max_concurrent_requests'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The number of maximum concurrent requests per replica to allow for this Webservice. Defaults to 1. Do not change this setting from the default value of 1 unless instructed by Microsoft Technical Support or a member of Azure Machine Learning team. 

`'max_request_wait_time'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The maximum amount of time a request will stay in the queue (in milliseconds) before returning a 503 error. Defaults to 500. 

`'num_replicas'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The number of containers to allocate for this Webservice. No default, if this parameter is not set then the autoscaler is enabled by default. 

`'primary_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
A primary auth key to use for this Webservice. 

`'secondary_key'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None   
A secondary auth key to use for this Webservice. 

`'tags'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None      
Dictionary of key value tags to give this Webservice. 

`'properties'` [dict](https://docs.python.org/3/library/stdtypes.html#dict)   
default value: None      
Dictionary of key value properties to give this Webservice. These properties cannot be changed after deployment, however new key value pairs can be added. 

`'description'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
A description to give this Webservice. 

`'gpu_cores'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The number of GPU cores to allocate for this Webservice. Defaults to 0. 

`'period_seconds'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
How often (in seconds) to perform the liveness probe. Default to 10 seconds. Minimum value is 1. 

`'initial_delay_seconds'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The number of seconds after the container has started before liveness probes are initiated. Defaults to 310.  

`'timeout_seconds'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The number of seconds after which the liveness probe times out. Defaults to 2 second. Minimum value is 1. 

`'success_threshold'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None     
The minimum consecutive successes for the liveness probe to be considered successful after having failed. Defaults to 1. Minimum value is 1. 

`'failure_threshold'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
When a Pod starts and the liveness probe fails, Kubernetes will try failureThreshold times before giving up. Defaults to 3. Minimum value is 1. 

`'namespace'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None     
The Kubernetes namespace in which to deploy this Webservice: up to 63 lowercase alphanumeric ('a'-'z', '0'-'9') and hyphen ('-') characters. The first and last characters cannot be hyphens. 

`'token_auth_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)    
default value: None      
Whether or not to enable Token auth for this Webservice. If this is enabled, users can access this Webservice by fetching an access token using their Azure Active Directory credentials. Defaults to False. 

`'compute_target_name'` [str](https://docs.python.org/3/library/stdtypes.html#str)  
default value: None      
The name of the compute target to deploy to. 

`'cpu_cores_limit'` [float](https://docs.python.org/3/library/functions.html#float)   
default value: None      
The max number of cpu cores this Webservice is allowed to use. Can be a decimal. 

`'memory_gb_limit'` [float](https://docs.python.org/3/library/functions.html#float)   
default value: None      
The max amount of memory (in GB) this Webservice is allowed to use. Can be a decimal. 

`'blobfuse_enabled'` [bool](https://docs.python.org/3/library/functions.html#bool)    
default value: None      
Whether or not to enable blobfuse for model downloading for this Webservice. Defaults to True.  

# **local deploy_config_args dictionary keyworded arguments to configure the webservice**

`'port'` [int](https://docs.python.org/3/library/functions.html#int)  
default value: None      
The local port on which to expose the service's HTTP endpoint. 
