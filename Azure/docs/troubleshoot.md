# **Troubleshooting**

## **Troubleshooting Kyma deployment**

### **Build and push to ACR failed. Ensure that the command 'az login --use-device-code' has been run for interactive authentication.**

If you get the above message during kyma deployment, perform the following steps:

- Open the terminal in the Azure ML Studio by referring the [(article)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-terminal#access-a-terminal)

- Run the command 'az login --use-device-code' in the terminal. Click on the link displayed in the terminal to open up a web browser and enter the authorization code displayed in your terminal. Follow rest of the steps displayed in the browser.

### **Assigning the 'acrpull' role to the service principal <SERVICE_PRINCIPAL_ID> to access the registry <acr_registry_id> failed.**

- Open the AzureML Workspace by referring the [(article)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=azure-portal#view)

- In the Workspace Overview page, click on the Registry link as shown below. This opens up the Azure Container Registry Overview page:

![Azure container registry link](acr.png)

- Follow the steps from step 2 of the [(article)](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal?tabs=current#step-2-open-the-add-role-assignment-page) to assign a 'ACRPull' role to Azure container registry as follows:

    -  In the Azure container registry page, follow step 2 of the article.

    -  In step 3, search for 'AcrPull' role.

    -  In step 4.3, search for the Service principal name you created in the Select box, select it and click next.

    -  Skip step 5 and follow step 6 to assign a ACRPull role to the Service Principal.
