import requests
import json
import model

url = "https://api.notion.com/v1/pages"
headers = {'Authorization': model.NOTION_SECRET,
            'Content-Type': 'application/json',
            "Notion-Version": '2021-08-16'}
payload = {"parent": { "type": "database_id", "database_id": model.DATABASE_ID},
            "properties": {"Name": {"type": "title","title": [{ "type": "text", "text": { "content": "Calisthenics" } }]},
            "Weight": {"type": "number","number": 170},
            "Pushups": {"type": "number","number": 100},
            "Active Calories": {"type": "number","number": 4200},
            "Total Calories": {"type": "number","number": 690},
            "Exercise Minutes": {"type": "number","number": 69}}}

payload_top_keys = ['parent', 'properties']
parent_nested_keys = ['type', 'database_id']
properties_top_keys = ['Name', 'Weight', 'Pushups', 'Active Calories', 'Total Calories', 'Exercise Minutes']



r = requests.post(url, data=json.JSONEncoder().encode(payload), headers=headers)

print(r.text)
