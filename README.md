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
- os
- json
- glob
- pd
- bigquery

## Working steps of this project
### Step 1: File Path Setup
##### 1.File Processing: 
- It starts by defining a filepath pointing to the directory containing JSON files (github_events_01.json).
- Then, it initializes an empty list all_files to store the absolute paths of all JSON files found in the directory and its subdirectories.
##### 2.File Enumeration:
- It uses os.walk() to recursively traverse the directory tree and gather a list of all JSON files found.
- For each file found, it appends the absolute file path to the all_files list.
##### 3.Counting Files:
- It calculates the total number of files found and prints a message displaying the count and the filepath.

```bash
ilepath = 'github_events_01.json'
all_files = []
for root, dirs, files in os.walk(filepath):
    files = glob.glob(os.path.join(root, "*.json"))
    for f in files:
        all_files.append(os.path.abspath(f))

num_files = len(all_files)
print(f"{num_files} files found in {filepath}")
```
### Step 2: Reading JSON Data
##### 1.Data Extraction:
- It initializes an empty list raw_d to store extracted data.
- It then iterates over each file in the all_files list.
- For each file, it opens it and loads the JSON data.
- For each entry (event) in the JSON data, it extracts user-related information from the payload section, specifically focusing on the issue object's user data.
- It extracts various attributes such as login, id, avatar_url, url, etc., from the user data and appends them to the raw_d list as a dictionary.
##### 2.Data Structure:
- The extracted data is structured into a dictionary format where each dictionary represents user-related information for an event.
##### 3.Continuation:
- The continue statement at the end of the loop ensures that the loop continues to the next iteration without executing any further code.
```bash
raw_d = []

with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)
    for each in data:
        issue_data = each['payload']['issue']['user']
        
        login = issue_data['login']
        user_id = issue_data['id']
        node_id = issue_data['node_id']
        avatar_url = issue_data['avatar_url']
        url = issue_data['url']
        html_url = issue_data['html_url']
        followers_url = issue_data['followers_url']
        following_url = issue_data['following_url']
        gists_url = issue_data['gists_url']
        starred_url = issue_data['starred_url']
        subscriptions_url = issue_data['subscriptions_url']
        organizations_url = issue_data['organizations_url']
        repos_url = issue_data['repos_url']
        events_url = issue_data['events_url']
        received_events_url = issue_data['received_events_url']
        user_type = issue_data['type']
        site_admin = issue_data['site_admin']
        
        raw_d.append({
            'login': login,
            'id': id,
            'node_id': node_id,
            'avatar_url': avatar_url,
            'user_id': user_id,
            'html_url': html_url,
            'followers_url': followers_url,
            'following_url': following_url,
            'gists_url': gists_url,
            'starred_url': starred_url,
            'subscriptions_url': subscriptions_url,
            'organizations_url': organizations_url,
            'repos_url': repos_url,
            'events_url': events_url,
            'received_events_url': received_events_url,
            'user_type': user_type,
            'site_admin': site_admin
        })
        continue
```
### Step 3: Creating DataFrame and save to BigQuery
- After extracting all the relevant data, it creates a Pandas DataFrame (df_raw) from the raw_d list.
- This line establishes a connection to BigQuery using the provided project ID.
- Finally, it loads the data from the DataFrame df_raw into a BigQuery table specified by dataset_id and table_id. If the table already exists, it will replace it with the new data (if_exists='replace'). If it doesn't exist, it will create a new table.



```bash
df_raw = pd.DataFrame(raw_d)

from google.cloud import bigquery

project_id = "------------"

# Dataset and table names
dataset_id = ""------------".Json_to_GCP"
table_id = "raw_json"

client = bigquery.Client(project=project_id)

# Load the DataFrame to BigQuery
df_raw.to_gbq(destination_table=f"{dataset_id}.{table_id}",
          project_id=project_id,
          if_exists='replace')
```