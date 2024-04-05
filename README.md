[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/data-warehouse-cloud-fedml)](https://api.reuse.software/info/github.com/SAP-samples/data-warehouse-cloud-fedml)

# FedML

## Description 
 
<br>

The SAP Federated ML Python libraries (FedML) applies the Data Federation architecture of SAP Datasphere for intelligently sourcing SAP as well as non-SAP data for Machine Learning experiments done at the ML platforms removing the need for replicating or moving data. 
By abstracting the Data Connection, Data load (for all ML platforms) and Model training (with flexibility and provision for user provided training scripts), Model Deployment, and Inferencing (for Hyperscaler Machine learning platforms) , the FedML library  provides end to end integration with few lines of code .

 ## What's New 
 
<b>1.</b> The new version of FedML (available as <b>fedml-dsp</b> in PyPi, V1.0.0) :
<ul><li>Is machine learning platform-independent. It can be used in all machine learning platforms
<li>Supports NVIDIA RAPIDS™, CUDA cuDF and cuPy and hence can be used for training models in GPU environments.
<li>Supports sourcing data from SAP Datasphere models directly into PySpark and cuPy (for GPU) dataframes.
<li>Supports SAP AI Core Deployment  - Models that are trained in any ML Platform (and containerized independently) can now be deployed in SAP GenAI Hub's AI Core with couple lines of code.
<li>Supports writing inferenced results back to SAP Datasphere.
 </ul>
 
 ### Solution Architecture 
 
 ![ARD](/FedMLNew.jpg)
 
<b>2.</b>FedML (Original, V2.0) for hyperscaler platforms [AWS, GCP, Azure and Databricks] :</font>
<ul><li>Is pip installable from PyPi for its respective hyperscaler platforms.
<li>Supports model training and deployment to hyperscaler environment.
<li>Supports deployment to SAP Business Technology Platform Kyma environment. 
<li>Supports inferencing with hyperscaler deployed as well as Kyma deployed models.
<li>Supports writing inferenced results back to SAP Datasphere.
</ul></ul>

### Solution Architecture - FedML Hyperscaler libraries
 
 ![ARD](/FedML_ARD.jpg)
 <br>


## Requirements 
 
- SAP Datasphere tenant instance, with connectivity established to the remote data sources, and views exposed, that can be consumed by FedML. 

- Access to corresponding  Machine learning Platforms with appropriate configurations. See [Configuration](#configuration) section.


## Download and Installation 

 Try out examples from the **samples-notebooks** directory of corresponding library folders

## Configuration 
- For FedML (platform-independent) library specific pre-requisites, configuration and documentation, [please refer here](Datasphere/fedml-dsp.md) <br>
- For AWS FedML library specific pre-requisites, configuration and documentation, [please refer here](AWS/fedml_aws.md) <br>
- For GCP FedML library specific pre-requisites, configuration and documentation, [please refer here](GCP/fedml_gcp.md)<br>
- For Azure FedML library specific pre-requisites, configuration and documentation, [please refer here](Azure/readme.md) <br>
- For Databricks FedML library specific pre-requisites, configuration and documentation, [please refer here](Databricks/README.md)<br><br>

## Limitations 

None
  <br>

## How to obtain support 

This project is provided "as-is" with no expectation for major changes or support. <br>
[Create an issue](/issues) in this repository if you find a bug or have questions about the content. <br>
For additional support, [ask a question](https://answers.sap.com/questions/ask.html) in SAP Community. 
   <br><br>

## Licensing 
 
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
<br>
