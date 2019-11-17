'''
author: Armeet Jatyani
year: 2019
purpose: fetches video search results
'''

#imports:
import os
import json
import requests
import time
import logging

#Youtube Data API v3 constants:
API_TOKEN = 'AIzaSyDfzZw-wSX8NfI2vamY38igjIkIMimv_eA'
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

#logging: 
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def get_vid_stats_id(id):
    #store response (string)
    full_response = ''

    #make request with params, store in response
    response = requests.get(API_URL_BASE + "/videos?part=id,statistics,snippet&id=" + id + "&key=" + API_TOKEN)

    #for debugging
    logging.debug("url: " + str(response.url))
    logging.debug("status code: " + str(response.status_code))

    #add to response
    full_response = full_response + response.text

    #return final response
    return full_response

def append_vid_stats(vid_resource):
    #open videoStats.json for reading and writing
    temp_file = open("./videoStats.json", "w+")

    #convert to python dict
    file_contents = temp_file.read()
    temp_dict = json.load(file_contents)
    #add our resource to the python dict
    temp_dict['videoStats'].add(json.load(vid_resource))
    
    #convert back to json and return
    temp_json = json.dump(temp_dict)
    
    #write back to file, close file
    temp_file.write(temp_json)
    temp_file.close()
   
#make request, find stats for vid with id, append to videoStats.json
response = get_vid_stats_id("8qvHQIJ4Y3k")
append_vid_stats(response)