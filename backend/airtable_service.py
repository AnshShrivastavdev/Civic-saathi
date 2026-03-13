import requests
import os

BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE = os.getenv("AIRTABLE_TABLE_NAME")
API_KEY = os.getenv("AIRTABLE_API_KEY")

url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE}"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def update_record(record_id, category):
    data = {
        "fields": {
            "Category": category,
            "Status": "Forwarded"
        }
    }

    response = requests.patch(f"{url}/{record_id}", json=data, headers=headers)

    if response.status_code not in (200, 201):
        raise Exception(
            f"Airtable update failed for record '{record_id}': "
            f"[{response.status_code}] {response.text}"
        )

    return response.json()
