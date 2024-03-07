# **Description**

The FedML library applies the data federation architecture with SAP Datasphere for intelligently sourcing the data in real-time from data storages. The library provides functionality that enables businesses and data scientists to build, train and deploy machine learning models on hyperscalers, without the hassle of replicating or migrating the data from the original data storage.

# **Prerequisites** 

The following steps needs to be completed in order to access the library functionality

- Creation of Azure Subscription  
In order to create an Azure ML Workspace, first you need access to an Azure subscription. You can create a [new subscription](https://azure.microsoft.com/en-us/free/?v=a&adobe_mc_sdid=SDID%3D17B51AC3059EF846-1FAC2DD18C4371FA%7CMCORGID%3DEA76ADE95776D2EC7F000101%40AdobeOrg%7CTS%3D1634155040) or access existing subscription information from the [Azure portal](https://portal.azure.com/).

- Creation of a Azure ML workspace  
Create an AzureML workspace from the Azure portal (recommended) or optionally through Python sdk. Please refer the [article](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal)

# **Documentation**

- For documentation of library class, methods and parameters, refer [fedml_azure.md](./docs/fedml_azure.md). 
- For documentation of how to use the library, refer [sample_notebooks](./sample-notebooks).
- For documentation on whitelisting single Azure IP in SAP Datasphere, refer [guide](./docs/whitelist_ip.md).

# **Troubleshooting**

The documentation for troubleshooting can be found [here](./docs/troubleshoot.md). 
