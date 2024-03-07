# **Steps to whitelist a single Azure public IP in SAP Datasphere:**

### Create a NAT gateway to expose a single public IP address  

1. Create a NAT Gateway with a public IP behind a virtual network by referring the [guide](https://learn.microsoft.com/en-us/azure/nat-gateway/quickstart-create-nat-gateway-portal). Ensure you create a virtual network with appropriate subnets.

### Attach the AzureML computes to the vnet and subnet created for the NAT gateway

2. Create an AzureML compute instance behind the same virtual network and subnet created in step 1 to run the AzureML notebook, by referring the [guide](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-compute-instance?view=azureml-api-2&tabs=azure-studio).

3. If you wish to use AzureML Compute cluster for training, you will need to set the `vnet_resourcegroup_name`, `vnet_name` and `subnet_name` in the `compute_args` parameter while creating the compute. You can find the parameters guide [here](https://github.com/SAP-samples/datasphere-fedml/blob/main/Azure/docs/parameters.md#compute_args-dictionary-keyworded-arguments).

For example:

```
compute=create_compute(workspace=workspace,
                   compute_type='AmlComputeCluster',
                   compute_args={'vm_size':'Standard_D12_v2',
                                'vnet_resourcegroup_name':'<vnet_resourcegroup_name-created-in-step1>',
                                'vnet_name':'<vnet_name-created-in-step1>',
                                'subnet_name':'<subnet-created-in-step1>'
                                }
                )
```

4. If you wish to deploy the model to ACI (Azure Container Instances), you will need to set `vnet_name` and `subnet_name` in the `deploy_config_args` parameter while creating the deployment as per the [guide](https://github.com/SAP-samples/datasphere-fedml/blob/main/Azure/docs/parameters.md#aci-deploy_config_args-dictionary-keyworded-arguments-to-configure-the-webservice).

For example:
```
aci_endpoint,_,aci_service=deploy(compute_type='ACI',
                                 inference_config_args={'entry_script':'<entry-script>', 'environment':environment},
                                 deploy_config_args={'cpu_cores':1, 'memory_gb':0.5,  'vnet_name':'<vnet_name-created-in-step1>'subnet_name':'<subnet-created-in-step1>'},
                                 deploy_args={'workspace':workspace,'name':'aciwebservice','models':[model]}
                                )
```
