#install the google cloud bigquery client services api
pip install google-cloud-bigquery

import os
import pandas as pd

from google.cloud import bigquery

#create a service account for the associated PROJECT_ID
#create a key for the service account on Cloud Console
#Download the key (json format) on your machine

credential_path = "<your_path>/<your_key>.jon"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

client = bigquery.Client()

query = """
    SELECT * FROM `<YOUR_PROJECT_ID>.<DATASET>.<TABLE>`
"""
query_job = client.query(query)
df = query_job.to_dataframe()
