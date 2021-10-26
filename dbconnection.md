# **DbConnection class**

DbConnection class abstracts the connectivity to SAP DataWarehouse Cloud, data query, data fetch and data load thereby reducing complexity and efficiently sourcing the data for the Hyperscaler Machine Learning environments with just couple lines of code.

## Pre-requisite :

config.json file present in main path <BR>

**<u>config.json</u>**
{

    "address":  <The IP address or host name of the database instance. Required. String>  ,
    "port": <The port number of the database instance. Required>,
    "user": <The database user. Required>,
    "password": <The database user's password. Required>,
    "schema": <The SAP Dataware house cloud Space Schema. Optional> ,
    "encrypt": <"true" . Denotes an encrypted connection>,
    "sslValidateCertificate": <"false" . Specifies whether to validate the server's certificate>,
    "disableCloudRedirect": < "true". Specifies if there should be a tenant redirection for a cloud instance),
    "communicationTimeout": <"0". Value of 0 Disables any communicaiton Timeouts> ,
    "autocommit": <"true". Sets auto commit to true for the database connection>,
    "sslUseDefaultTrustStore": <"true". Denotes the use of client's default trust store >
}
<br>



## Constructor
 
DBConnection()

## Class Methods

1. **get_schema_views()** : <br>
Returns the list of all View names in the Space Schema . <br>
Parameters: None
<br> <br>

2. **get_table_size(`'table_name'`)**:<br> Returns the count of rows ( [int](https://docs.python.org/3/library/functions.html#int) ) in the existing schema object <br>
Parameter: `'table_name':` [str](https://docs.python.org/3/library/stdtypes.html#str)  
 <br><br>
3. **get_data_with_headers(`'table_name'`,`'size=1'`)**:
<br> Returns the data fetched from Schema view. <br>
Parameters :<br> 
`'table_name':`  [str](https://docs.python.org/3/library/stdtypes.html#str)  <br>
`'size'` ( [int](https://docs.python.org/3/library/functions.html#int) )  : Number or rows to fetch from the Schema view <br> 
<br><br>
4. **execute_query(`'query'`)**:
<br> Executes the SQL Query and returns the data fetched . <br>
Parameter :<br> 
`'query':`  [str](https://docs.python.org/3/library/stdtypes.html#str)  <br>


