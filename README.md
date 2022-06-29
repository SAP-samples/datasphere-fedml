[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/data-warehouse-cloud-fedml)](https://api.reuse.software/info/github.com/SAP-samples/data-warehouse-cloud-fedml)

# FedML

## Description 
 
<br>

The SAP Federated ML Python libraries (FedML) applies the Data Federation architecture of SAP DataWarehouse Cloud for intelligently sourcing SAP as well as  non-SAP data for Machine Learning experiments done at the Hyperscalers thereby removing the need for replicating or moving data. 
By abstracting the Data Connection, Data load, and Model training (with flexibility and provision for user provided training scripts), Model Deployment, and Inferencing for Hyperscaler Machine learning processes , the FedML library  provides end to end integration with few lines of code .


 ## What's New 

Here are some high level major feature additions in Version 2.0 of FedML:

<ul><li>FedML is now pip installable from PyPi repo.
<li> Support for deployment to hyperscaler environment.
<li>Support for deployment to SAP Business Technology Platform Kyma environment. 
<li>Support for inferencing with hyperscaler deployed as well as Kyma deployed models.
<li>Support for writing inferenced results back to SAP Data Warehouse Cloud.
</ul>
<br>

## Solution Architecture
 
 ![ARD](/FedML_ARD.jpg)
 <br>


## Requirements 
 
- SAP Data Warehouse Cloud tenant instance, with connectivity established to the remote data sources, and views exposed, that can be consumed by FedML. 

- Access to corresponding Hyperscaler Machine learning environments with approriate configurations. See [Configuration](#configuration) section.
<br>

## Download and Installation 

1. Try out examples from the **samples-notebooks** directory of corresponding Hyperscaler library 

2. For setting up the remote models in SAP DataWarehouse Cloud to federate data from hyperscaler data stores for use with FedML , here are some Discovery Mission examples :

- [Integrating Amazon Athena and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3401/3441/)
- [Integrating Google Big Query and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3409/3449/)
- [Integrating Azure Data Explorer and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3433/3473/)

 <br>

## Configuration 

- For AWS FedML library specific pre-requisites, configuration and documentation, [please refer here](AWS/fedml_aws.md) <br>
- For GCP FedML library specific pre-requisites, configuration and documentation, [please refer here](GCP/fedml_gcp.md)<br>
- For Azure FedML library specific pre-requisites, configuration and documentation, [please refer here](Azure/readme.md) <br><br>


## Limitations 

None
  <br><br>

## How to obtain support 

This project is provided "as-is" with no expectation for major changes or support. <br>
[Create an issue](/issues) in this repository if you find a bug or have questions about the content. <br>
For additional support, [ask a question](https://answers.sap.com/questions/ask.html) in SAP Community. 
   <br><br>

## Licensing 
 
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
<br>
