import requests

BASE_ID='apptrqIGtq0fF9Kpy'
API_KEY='keyGYvfJ0W9ZYl9lb'
TABLE_NAME='Aggregated%20all%20time'
endpoint='https://api.airtable.com/v0/apptrqIGtq0fF9Kpy/Aggregated%20all%20time'
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
  "records": [
    {
      "id": "reczO6dx7hyro6uzE",
      "fields": {
        "paper_sheet_count": 5001,
      }
    },
  ]
}

r = requests.patch(endpoint, json= data, headers=headers)
print(r.json())