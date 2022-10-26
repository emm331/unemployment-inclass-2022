
# this is the app/unemployment_report.py file

import os
import json
from pprint import pprint

import requests

# this is where we specify the name of API variable
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = "https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

from getpass import getpass

API_KEY = getpass("Please input your AlphaVantage API Key: ") 

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

data = parsed_response["data"]