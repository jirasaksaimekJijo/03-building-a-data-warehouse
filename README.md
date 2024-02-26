# Week 3: ETL Pipeline for a Cloud Data Warehouse (Google BigQuery)

## Description
Google BigQuery is a fully managed, serverless, and highly scalable cloud data warehouse provided by Google Cloud Platform (GCP). 
It allows you to analyze big data using SQL queries without the need for managing infrastructure. With BigQuery, you can store and query massive datasets quickly and efficiently, making it suitable for analytics, business intelligence, machine learning, and other data-driven tasks.

To load JSON data into Google BigQuery, prepare your data, create a dataset, define the schema, load the data using the web UI, bq tool, or API, then verify and query it.

## Prosesc
1. Create Dataset:
- In Google BigQuery, we first create a Dataset to serve as the storage area for our data. A Dataset is similar to a database in   traditional RDBMS. We can use the BigQuery UI, bq command-line tool, or API to create a Dataset, specifying the name and other parameters as needed.

2. Create Table:
- Once the Dataset is created, the next step is to create a Table to store our data. We use the BigQuery UI, bq command-line tool, or API to define the name of the table and the schema of the data to be stored.

3. Import JSON Data:
- After creating the Dataset and Table, we can use the BigQuery web UI, bq tool, or API to import data from the JSON file into the created table. We can directly upload JSON files using the BigQuery UI or use the bq command-line tool to load data from local files or Google Cloud Storage.

4. Querying:
- Once the data is successfully imported, we can use SQL queries in BigQuery to query, modify, or delete data as needed.

## Library Python

If you want to consolidate all the libraries and versions into one file for installation in one go, you can use either a requirements.txt file or an environment.yml file. These are convenient and efficient ways to manage dependencies for your project.

- equirements.txt: This file specifies the names of the libraries and the versions to be installed. You can create one like this:
```bash
numpy==1.23.2
psycopg2==2.9.3
python-dateutil==2.8.2
pytz==2022.2.1
six==1.16.0
```
## 
The command you would use to install libraries, and once executed, the specified libraries will be ready to use. 

```bash
pip install -r requirements.txt
```
- numpy
- psycopg2
- python-dateutil
- pytz
- six

## Working steps of this project
### Step 1: 
### Step 2:
### Step 3: 
