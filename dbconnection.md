# **DbConnection class**

DbConnection class abstracts the connectivity to SAP DataWarehouse Cloud, data query, data fetch and data load thereby reducing complexity and efficiently sourcing the data for the Hyperscaler Machine Learning environments with just couple lines of code.

## Pre-requisite:

config.json file present in main path <BR>

**<u>config.json</u>**
{

    "address":  <The IP address or host name of the database instance. Required. String>,
    "port": <The port number of the database instance. Required>,
    "user": <The database user. Required>,
    "password": <The database user's password. Required>,
    "schema": <The SAP Dataware house cloud Space Schema. Optional>,
    "encrypt": <"true" . Denotes an encrypted connection>,
    "sslValidateCertificate": <"false" . Specifies whether to validate the server's certificate>,
    "disableCloudRedirect": < "true". Specifies if there should be a tenant redirection for a cloud instance),
    "communicationTimeout": <"0". Value of 0 Disables any communicaiton Timeouts>,
    "autocommit": <"true". Sets auto commit to true for the database connection>,
    "sslUseDefaultTrustStore": <"true". Denotes the use of client's default trust store>
}
<br>

**Setting up your config.json**
1. Navigate to the space management inside DWC 
<br>
<img src="space_management.png" alt="space management" height="500">
<br>
2. Navigate to database users.

![databaseusers](database_users.png)
<br>
3. Create a user if you don't already have one with Read and Write privileges.

![createuser](create_user.png)
<br>
4. Click on the i icon.

![userprivileges](user_privileges.png)

Here you will find the following information for your config.json: <br>
- Database User Name --> `user`
- Space Schema --> `schema`
- Host Name --> `address`
- Port --> `port`
- Password --> `password`
<br>

## Constructor
 
**DBConnection(`'package_name=None'`, `'url=None'`)**<br>
Parameters: <br>
`'package_name':` ([str](https://docs.python.org/3/library/stdtypes.html#str)): The package name used for fedml_gcp.<br>
`'url':` ([str](https://docs.python.org/3/library/stdtypes.html#str)): The url path (if not stored in root) of where to find the config.json<br>
Examples: <br>
`db = DbConnection()`<br>
`db = DbConnection(package_name='trainer')`

## Class Methods

1. **get_schema_views()**:<br>
Returns the list of all View names in the Space Schema. <br>
Parameters:<br>
None<br>
Example: <br>
`db.get_schema_views()`
<br> <br>

2. **get_table_size(`'table_name'`)**:<br> 
Returns the count of rows ([int](https://docs.python.org/3/library/functions.html#int)) in the existing schema object <br>
Parameter: <br>
`'table_name'` [(str](https://docs.python.org/3/library/stdtypes.html#str)): The name of the table.<br>
Example: <br>
`db.get_table_size('TITANIC_VIEW')`
<br> <br>

3. **get_data_with_headers(`'table_name'`,`'size=1'`)**: <br>
Returns the data fetched from Schema view. <br>
Parameters: <br> 
`'table_name'` ([str](https://docs.python.org/3/library/stdtypes.html#str)): The name of the table.<br>
`'size'` ([int](https://docs.python.org/3/library/functions.html#int)): Number or rows to fetch from the Schema view<br>
Example:<br>
`db.get_data_with_headers(table_name='IRIS_VIEW', size=1)`
<br> <br>

4. **execute_query(`'query'`)**: <br> 
Executes the SQL Query and returns the data fetched. <br>
Parameter: <br> 
`'query'`  ([str](https://docs.python.org/3/library/stdtypes.html#str)): The SQL query to execute<br>
Example:<br>
`db.execute_query('SELECT * FROM ' + config['schema'] +'.SALES_VIEW')`
<br><br>

5. **create_table(`'query'`)**: <br> 
Created a table in DWC. <br>
Please note this function will create a default column called `INSERTED_AT` in the table specified. This column will keep track of the timestamp at which you inserted data into the table for the first time.<br>
Parameter: <br> 
`'query'`  ([str](https://docs.python.org/3/library/stdtypes.html#str)): The SQL query to create a table.<br>
Example:<br>
`db.create_table("CREATE TABLE T6 (ID INTEGER PRIMARY KEY, C2 VARCHAR(255))")`
<br><br>

6. **insert_into_table(`'table_name'`, `'table_values'`)**: <br> 
Inserts data into the table specified. <br>
Please note this function will insert the current timestamp into a column called `INSERTED_AT` in the table specified. <br>
Parameter: <br> 
`'table_name'`  ([str](https://docs.python.org/3/library/stdtypes.html#str)): The table name. <br>
`'table_values'`  ([Pandas DataFrame](https://pandas.pydata.org/docs/reference/frame.html)): The data to insert.<br>
Example:<br>
`sample_df = pd.DataFrame([[6,'hey6'],[7,'bye7']], columns=['id', 'c2'])`<br>
`db.insert_into_table('T6', sample_df)`
<br><br>

7. **drop_table(`'table_name'`)**: <br> 
Drops table specified. <br>
Please note this function only deletes the DB Users table. If this table was deployed in DWC and/or has a view attached, you will need to delete those manually in DWC. <br>
Parameter: <br> 
`'table_name'`  ([str](https://docs.python.org/3/library/stdtypes.html#str)): The table name. <br>
Example:<br>
`db.drop_table('T6')`
<br><br>