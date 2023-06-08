# **Troubleshooting Steps**

1. Error while executing `execute_query_pyspark`  and `get_data_with_headers_pyspark` methods:  
`ERROR: error occured while retrieving the data as PySpark dataframe.Use the "execute_query" method to get the data. 'DataFrame' object has no attribute 'iteritems'`  

    Solution:   
        - Upgrading the Databricks Runtime Version of the databricks cluster to a version compatible with Spark 3.4 (DBR 13.x or later).  
        - Downgrading pandas to version lower than 2.0  

2. If you get an error similar to the below image while running `deploy_to_kyma` method, please ensure that you have a python version compatible with the latest version of mlflow which can be found [here](https://pypi.org/project/mlflow/) and install the latest version of mlflow.
![protobuferror](protobuf_error.png)
