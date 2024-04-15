# **fedml_dsp**

fedml_dsp currently supports the ability to deploy ml models to SAP AI Core

<br/>

# **DbConnection class**

Please note that to use the cupy and cuml functions, you must import DbConnection. This is done as:
`from fedml-dsp import DbConnection`

For more information regarding the DbConnection class, please refer to the [dbconnection READme](../../dbconnection.md)

# **Fedml class**

## **Prerequisites**

- To deploy a ML model to AI Core, you must have a docker image published somewhere (i.e. AWS ECR, dockerhub, Azure ACR, GCP Container Registry, etc.)
- You must also already have AI Core enabled in your BTP account.

## **Installing the Library**
`pip install fedml-dsp`

## **Importing the Library**
`from fedml_dsp import Fedml`

## **Constructor**

`Fedml(ai_service_key)`

Initializes the connection to AI Core.

### **Parameters**:

`ai_service_key` [(str)](https://docs.python.org/3/library/stdtypes.html#str): Your ai core service key JSON file relative to thee notebook you are using the FedML DSP library in.

You can create a AI Core Service Key by following these steps [(here)](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/create-service-key) and [(here)](https://developers.sap.com/tutorials/ai-core-setup.html)

### **Example of use**:

`fedml = Fedml(aic_service_key='aic_service_key.json')`

## **Deploying a Machine Learning Model to SAP AI Core**

### **Step 1**:
First, you will need to onboard any ai core resources needed. These include your github repository, AI core resource group, and secret to provide AI core pull permissions to your docker registry.

**`onboard_ai_core(resource_group, github_info_path, create_resource_group=False, onboard_new_repo=False, secret_path=None)`**

#### **Parameters**:

**`resource_group` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

The AI Core resource group you are using. If you are creating this resource group, you must provide `True` to the `create_resource_group` parameter.

**`github_info_path` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

A path to a JSON file containing the information needed for github access. Recall the importance of GitHub with SAP AI Core by reviewing this documentation [(here)](https://developers.sap.com/tutorials/ai-core-helloworld.html). You do not need to complete all of these steps. Only steps 1 and 2 are relevant for creating the Github PAT.

The format of this json file is as follows:
```
{
    "name": "<SAP AI Core resource group>",
    "url": "<Github url>",
    "username": "<Github username>",
    "password": "<Github PAT. Follow the tutorial Steps 1 & 2 given above for steps on how to create this>"
}
```

**`create_resource_group` [(bool)](https://docs.python.org/3/library/functions.html#bool):**

`True` if you want to create a resource group in SAP AI Core. `False` if you do not (i.e., you are using an existing one).

**`onboard_new_repo` [(bool)](https://docs.python.org/3/library/functions.html#bool):**

`True` if you want to onboard a new Github repo to SAP AI Core. `False` if you do not (i.e., you are using an existing one).

**`secret_path` [(str)](https://docs.python.org/3/library/stdtypes.html#str):**

The path where your docker registry secret file (JSON) is located relative to the notebook you are running this library in. This file should have the following structure:
```
{
    "name": "secretname",
    "data": {
        ".dockerconfigjson": "{\"auths\":{\"YOUR_DOCKER_REGISTRY_URL\":{\"username\":\"YOUR_DOCKER_USERNAME\",\"password\":\"YOUR_DOCKER_ACCESS_TOKEN\"}}}"    
        }
}
```

If you are using AWS, please follow [(this)](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html]) to generate the secret
If you are using GCP, please follow [(this)](https://cloud.google.com/artifact-registry/docs/docker/authentication#json-key) to generate the secret.
Other docker container registries are supported as well. Please find your container registries authorization information accordingly.

#### **Example of use**:
```
fedml.onboard_ai_core(create_resource_group=False, resource_group='ai-core-test2', onboard_new_repo=False,github_info_path="github_info.json", secret_path="secret.json")
```

### **Step 2**:
Next, you need to register the application you want to use in AI Core. You only need to perform this step when you need to register a new application. So if you are using an already existing AI Core application for your deployment, skip this step. 

**`register_application(application_details)`**

#### **Parameters**:

**`application_details` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict):**

The format of this dictionary is:
```
{
    "application_name": "<application name>",
    "revision": "<the commit (HEAD or a number for the revision commit to point to) in github>",
    "repository_url": "<github url. NOT down to the path of the application. Just the repo.>",
    "path": "<the folder for which the applications serving executable yaml is located>"
}
```
For information on how to create and structure a serving executable yaml, please refer to this [(tutorial)](https://developers.sap.com/tutorials/ai-core-code.html)

An example of the YAML is also shown here:
```
apiVersion: ai.sap.com/v1alpha1
kind: ServingTemplate
metadata:
  name: <your chosen name>
  annotations:
    scenarios.ai.sap.com/description: "<a scenario description>"
    scenarios.ai.sap.com/name: "<your chosen scenario name>"
    executables.ai.sap.com/description: "<a description>"
    executables.ai.sap.com/name: "<your chosen executable name>"
  labels:
    scenarios.ai.sap.com/id: "<your chosen id>"
    ai.sap.com/version: "1.0.0"
spec:
  inputs:
    artifacts:
      - name: modelArtifact
  template:
    apiVersion: "serving.kubeflow.org/v1beta1"
    metadata:
      labels: |
        ai.sap.com/resourcePlan: infer.s
    spec: |
      predictor:
        imagePullSecrets:
          - name: <secret for which you are using to authenticate to the container registry. this is the secret you onboarded earlier.>
        containers:
        - name: kfserving-container
          image: "<image as given by your container registry>" #replace this
          ports:
            - containerPort: <port>
              protocol: TCP
```
Note the repository_url here must already be onboarded with aicore. if not please use the onboard_ai_core() function to onboard it.

#### **Example of use**:
Suppose your application details were as follows:

```
application_details = 
{ 
    "application_name": "application1", 
    "revision": "HEAD", 
    "repository_url": "https://github.com/username/repo_name", 
    "path": "applicationyamlpath"
}
```
The path in the above dictionary should only be the path to the yaml folder.

You would then pass this dictionary to the function as so:
`fedml.register_application(application_details=application_details)`

If the registration was successful, you should get a message stating that. Otherwise, the error should be shown to you.

### **Step 3**:
Following, you can begin your deployment to AI Core.

**`ai_core_deploy(deployment_config)`**<br>
Returns an endpoint

#### **Parameters**:
**`deployment_config` [(dict)](https://docs.python.org/3/library/stdtypes.html#dict):**

The format of this dictionary is as follows:
```
{
    "name": "<application name>", 
    "resource_group": "<resource group name>", 
    "scenario_id": "<scenario id>", 
    "executable_id": "<executable id>"
}
```

- name should be the name of the AI Core application you have been referencing throughout your code for deployment.
- resource_group should be resource group you've been using for SAP AI Core throughout this notebook
- scenario_id should be the scenario_id in the serving executable yaml in the github workflow you created
- executable_id should be the executable_id in the serving executable yaml in the github workflow you created

#### **Example of use**:
```
deployment_config = 
{
    "name": "applicationname", 
    "resource_group": "resourcegroupname", 
    "scenario_id": "scenarioid", 
    "executable_id": "executableid"
}
```

`endpoint = fedml.ai_core_deploy(deployment_config=deployment_config)`

**Note:** our logger currently returns a `/v2/invocations` example endpoint for inferencing the deployed model. This endpoint value should be adapted to whatever is defined as the inference endpoint in your deployed container. Commonly, this is referred to as `/v2/predict` in [SAP AI Core inferencing tutorials](https://developers.sap.com/tutorials/ai-core-deploy.html).

### **Step 4**:
Finally, after deployment is done, you can inference your model

**`ai_core_inference(endpoint, headers, body)`**<br>
Returns a inference response

#### **Parameters**:
**`endpoint`[(str)](https://docs.python.org/3/library/stdtypes.html#str):**
The api endpoint that was returned from the `ai_core_deploy(...)` function. The api endpoint is also printed to the logs and can be found in AI Core Launchpad if needed to reference again.

**`headers`[(dict)](https://docs.python.org/3/library/stdtypes.html#dict):**

The headers needed for inferencing.
```
{
    "Authorization": <Authorization token. Please refer to the `get_ai_core_token()` function below>,
    "ai-resource-group": "<ai core resource group>", 
    "Content-Type": "<content type of data inferencing. this is specific to your model you are deploying.>"
}
```

**`body`[(dict)](https://docs.python.org/3/library/stdtypes.html#dict):**
The data to which you want to pass to your endpoint for predictions.

**get_ai_core_token()**
To get the authorization token needed to authorize inferencing calls to SAP AI Core.

#### **Example of use**:

```
endpoint = 'https://endpoint.com'

headers = {
    "Authorization": fedml.get_ai_core_token(),
    "ai-resource-group": "aicoreresourcegroup",
    "Content-Type": "text/csv"}

data = {}

response_data = fedml.ai_core_inference(endpoint=endpoint,headers=headers,body=X.to_json())
```

