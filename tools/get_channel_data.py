import os
import json
import requests
import time

API_TOKEN = 'AIzaSyCqWZpaWln53yBER6LFp1gqkgyRNJEzF8g'
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

def search_vids_keyword(search_keyword, starting_page_token):
    full_response = ''
    next_page_token = starting_page_token
    while next_page_token != 'end':
        response = requests.get(API_URL_BASE + "/search?part=snippet&prettyPrint=true&maxResults=50&q=a&key=" + API_TOKEN + "&pageToken=" + next_page_token)
        loaded_response = json.loads(response.content)
        print(response.content)
        try:
            next_page_token = loaded_response['nextPageToken']
        except:
            next_page_token = 'end' 
        print(next_page_token)
        full_response = full_response + json.dumps(loaded_response)
        time.sleep(30);
    return full_response;
    
f = open("tools/response.json","w+")
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i = 0
while i < len(arr):
    response = search_vids_keyword(arr[i], "");
    f.write((response))
    i = i + 1;
f.close();