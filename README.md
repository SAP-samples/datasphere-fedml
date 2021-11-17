[![REUSE status](https://api.reuse.software/badge/GitHub.com/SAP-samples/dwc-fedml)](https://api.reuse.software/info/GitHub.com/SAP-samples/dwc-fedml)

# FedML: Federated Machine Learning

## Description 
 
<br>

The SAP Federated Machine Learning Python libraries (FedML) applies the data federation architecture of SAP Data Warehouse Cloud for sourcing the data in real time for machine learning experiments done at the hyperscalers thereby removing the need for replicating or moving data.

By abstracting the data connection, data load, and model training (with flexibility and provision for user provided training scripts) for hyperscaler machine learning processes, the FedML library provides end to end integration with few lines of code. This repo contains sample code to show how to use FedML libraries.

This project is at an early validation phase and is not meant to be used productively. 

## Solution Architecture
 
 ![ARD](/FedML_ARD.jpg)
 <br>
<br>
## Requirements 
 
- SAP Data Warehouse Cloud tenant instance, with connectivity established to the remote source data and views exposed, that can be consumed by FedML. 

- Access to corresponding hyperscaler machine learning environments with approriate configurations. See [Configuration](#configuration) section.
<br>
 <br>

## Download and Installation 

1. For setting up the remote models in SAP DataWarehouse Cloud to federate data from hyperscaler data stores for use with FedML, here are some Discovery Mission examples:

- [Integrating Amazon Athena and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3401/3441/)
- [Integrating Google Big Query and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3409/3449/)
- [Integrating Azure Data Explorer and SAP DataWarehouse Cloud](https://discovery-center.cloud.sap/missiondetail/3433/3473/)

2. Download the corresponding hyperscaler library package (.whl) file from this repository

3. Try out examples from the **samples-notebooks** directory of corresponding hyperscaler library 


 <br>

## Configuration 

- For AWS FedML library specific pre-requisites, configuration and documentation, [please refer here](AWS/readme.md) <br>
- For GCP FedML library specific pre-requisites, configuration and documentation, [please refer here](GCP/fedml_gcp.md)<br>
- For Azure FedML library specific pre-requisites, configuration and documentation, [please refer here](Azure/readme.md) <br><br>


## Limitations 

None.
  <br><br>

## How to obtain support 

This project is provided "as-is" with no expectation for major changes or support. <br>

[Create an issue](https://github.com/SAP-samples/dwc-fedml/issues) in this repository if you find a bug or have questions about the content. <br>

For additional support, [ask a question](https://answers.sap.com/questions/ask.html) in SAP Community. 
   <br><br>
   
## To-Do (upcoming changes) 

Future expanded scope for the library will inlcude Deployment and Inference support.
 
## Licensing 
 
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
<br>
<br>
