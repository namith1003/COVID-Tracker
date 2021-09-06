import requests
import json
import pandas as pd

# POST to API
payload = {'code': 'ALL'} # or {'code': 'DE'}
URL = 'https://api.statworx.com/covid'
response = requests.post(url=URL, data=json.dumps(payload)) #dumps convert python object into string

# Convert to data frame
df = pd.DataFrame.from_dict(json.loads(response.text)) #loads used to parse a valid JSON string and convert it into a Python Dictionary.
print(df.head())