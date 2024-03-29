# **Description**

The SAP Federated ML Python library for Databricks applies the Data Federation architecture of SAP Datasphere for intelligently sourcing SAP as well as non-SAP data for Machine Learning experiments done in Databricks, thereby removing the need for replicating or moving the data. By abstracting the Data Connection, Data load, Model Deployment in SAP environment, and Inferencing for Machine learning processes , the FedML Databricks library provides end-to-end integration with few lines of code.

# **Prerequisites** 

1. Create a Databricks workspace in any of the three supported hyperscalers ([AWS](https://docs.databricks.com/administration-guide/account-settings-e2/workspaces.html), [Azure](https://learn.microsoft.com/en-us/azure/databricks/security/network/secure-cluster-connectivity#use-secure-cluster-connectivity)).

2. Create a cluster in the Databricks portal by referring to the [guide](https://learn.microsoft.com/en-us/azure/databricks/clusters/create-cluster). 

3. Create a notebook in the Databricks portal by referring to the [guide](https://learn.microsoft.com/en-us/azure/databricks/notebooks/notebooks-manage). 

4. Whitelist the Databricks cluster IP in SAP Datasphere by referring to this [guide](docs/whitelist_ip.md). 

# **Documentation**

For documentation on SAP Datasphere Core Connectivity methods, please refer [(DbConnection)](../dbconnection.md) 

For documentation on FedML Databricks SAP Kyma Kubernetes deployment and inferencing methods, please refer [(FedML Databricks Deployment/Inferencing)](docs/fedml_databricks.md).  

For getting started with the FedML Databricks Library, please refer the sample notebooks [(Sample notebooks)](./sample-notebooks).

# **Troubleshooting**

For steps on troubleshooting, plese refer to this [guide](docs/troubleshooting.md).