# **Description**

The Library initializes the resources required for the model training, enables the training data to be read from SAP DWC in real time without storing it in any Azure Storage, trains a Machine Learning model and registers it. 

# **Prerequisites** 

The following steps needs to be completed in order to access the library functionality

- Creation of Azure Subscription  
In order to create an Azure ML Workspace, first you need access to an Azure subscription. You can create a [new subscription](https://azure.microsoft.com/en-us/free/?v=a&adobe_mc_sdid=SDID%3D17B51AC3059EF846-1FAC2DD18C4371FA%7CMCORGID%3DEA76ADE95776D2EC7F000101%40AdobeOrg%7CTS%3D1634155040) or access existing subscription information from the [Azure portal](https://portal.azure.com/).

- Creation of a Azure ML workspace  
Create an AzureML workspace from the Azure portal (recommended) or optionally through Python sdk. Please refer the [article](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal)

# **Documentation**

- For documentation of library class, methods and parameters, refer [fedml_azure.md](./docs/fedml_azure.md)  
- For documentation of how to use the library, refer [sample_notebooks](./sample-notebooks/version_2_sample_notebooks)

# **Troubleshooting**

The documentation for troubleshooting can be found [here](./docs/troubleshoot.md).

# **Additional Information**

- The library has not been tested with [SGS baseline control policy- Ensure container registries are private](https://jam4.sapjam.com/articles/KvavoUCgXGlWYIUbgvcFnL)
