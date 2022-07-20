#install google bigquery client services library
pip install google-cloud-bigquery

import os
import json

from google.cloud import bigquery

#create a service account for the associated PROJECT_ID
#create a key for the service account on Cloud Console
#Download the key (json format) on your machine

credential_path = "<your_path>/<your_key>.jon"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

client = bigquery.Client()

#consider your data is of numpy array type.
#since numpy is JSON serializable, you can convert it into a list
arr = data.tolist()

#you can also convert the numpy array into a json object by encoding it:
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

json_dump = json.dumps({"<preferred_dict_name>": data}, cls=NumpyEncoder)
print(json_dump)

table_id = "<PROJECT_ID>.<DATASET>.<TABLE>"

rows_to_insert = [
    {u'<column_name>': arr[0]},
    {u'<column_name>': arr[1]},
    {u'<column_name>': arr[2]},
    {u'<column_name>': arr[3]},
    {u'<column_name>': arr[4]},
    {u'<column_name>': arr[5]},
    {u'<column_name>': arr[6]},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("Predictions have been added to BigQuery")
else:
    print(f'Encountered errors while adding predictions to BigQuery: {errors}')

