import os
import json
import glob
import pandas as pd
from google.cloud import bigquery

filepath = 'github_events_01.json'
all_files = []
for root, dirs, files in os.walk(filepath):
    files = glob.glob(os.path.join(root, "*.json"))
    for f in files:
        all_files.append(os.path.abspath(f))

num_files = len(all_files)
print(f"{num_files} files found in {filepath}")

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
    
df_raw = pd.DataFrame(raw_d)

from google.cloud import bigquery

project_id = "plenary-justice-389205"

# Dataset and table names
dataset_id = "plenary-justice-389205.Json_to_GCP"
table_id = "raw_json"

client = bigquery.Client(project=project_id)

# Load the DataFrame to BigQuery
df_raw.to_gbq(destination_table=f"{dataset_id}.{table_id}",
          project_id=project_id,
          if_exists='replace')