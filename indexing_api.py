import json
import requests
import time
import csv
from oauth2client.service_account import ServiceAccountCredentials

def index_url(url):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'some.json',  # Your service account key file
        ['https://www.googleapis.com/auth/indexing']
    )

    access_token_info = credentials.get_access_token()

    endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    content = {
        'url': url,  # The URL of the page to be indexed
        'type': 'URL_UPDATED'  # Or URL_DELETED if the page was removed
    }

    response = requests.post(
        endpoint,
        data=json.dumps(content),
        params={'access_token': access_token_info.access_token},
        headers={'Content-Type': 'application/json'}
    )

    print(response.content)


def read_urls_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            index_url(row[0])  # URL is in the first column
            time.sleep(1)  # Sleep for 1 second between requests


# Replace 'urls.csv' with the path to your CSV file
read_urls_from_csv('urls.csv')
