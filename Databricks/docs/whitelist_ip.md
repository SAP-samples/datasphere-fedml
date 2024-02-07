# **Steps to whitelist the Databricks Cluster IP in SAP Datasphere:**

Note: You will need a non-community version of Databricks account to perform the below steps. For a trial Databricks account, you can whitelist “0.0.0.0/0” in SAP Datasphere by referring this [guide](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/a3c214514ef94e899459f68f4c1e2a23.html) and skip the below steps.

## For Azure Databricks: 

Ensure that you have created an Azure Databricks Workspace with secure cluster connectivity as listed in the pre-requisites section. If not already created, create it by referring to the [article](https://learn.microsoft.com/en-us/azure/databricks/security/network/secure-cluster-connectivity#use-secure-cluster-connectivity). 

In the overview page of the created Azure Databricks Workspace, navigate to "Managed Resource Group". Search for "NAT gateway" in the overview page of the Managed Resource Group and navigate to the NAT gateway. 

In the overview page of the NAT Gateway, click on "Outbound IP" under “Settings” and take a note of the IP address under “Public IP addressess”. Whitelist this IP address in SAP Datasphere by referring to the [guide](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/a3c214514ef94e899459f68f4c1e2a23.html). 

## For AWS Databricks: 

Ensure that you have created a Databricks workspace in AWS as listed in the pre-requisites section. If not already created, create it by referring to the [article](https://docs.databricks.com/administration-guide/workspace/create-workspace.html).

Navigate to VPC Dashboard in the same region as the Databricks Workspace. 

On the VPC Dashboard, navigate to "NAT Gateways". Select the NAT Gateway associated with the Databricks VPC and copy the IP address listed under "Primary public IPv4 address". Whitelist this IP address in SAP Datasphere by referring to the [guide](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/a3c214514ef94e899459f68f4c1e2a23.html). 
