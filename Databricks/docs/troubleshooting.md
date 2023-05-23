# **Troubleshooting Steps**

1. Error while executing `execute_query_pyspark`  and `get_data_with_headers_pyspark` methods:  
`ERROR: error occured while retrieving the data as PySpark dataframe.Use the "execute_query" method to get the data. 'DataFrame' object has no attribute 'iteritems'`  

    Solution:   
        - Upgrading the Databricks Runtime Version of the databricks cluster to a version compatible with Spark 3.4 (DBR 13.x or later).  
        - Downgrading pandas to version lower than 2.0  
