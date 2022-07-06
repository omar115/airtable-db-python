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
      "fields": {
        "teacher_id": 2,
        "paper_sheet_count": 1235,
        "online_sheet_count": 3000,
        "paper_assessment_count": 20,
        "online_assessment_count": 20
      }
    },
  ]
}

r = requests.post(endpoint, json= data, headers=headers)
print(r.json())