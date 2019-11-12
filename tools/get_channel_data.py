import os
import json
import requests

API_TOKEN = os.environ['DEVELOPER_KEY'];
API_URL_BASE = 'http://api.wolframalpha.com/v1/simple?appid=DEMO'

response = requests.get(API_URL_BASE + "&i=What+airplanes+are+flying+overhead%3F")
print(response)
