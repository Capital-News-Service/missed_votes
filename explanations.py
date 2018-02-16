#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:33:32 2018

@author: gmkanik
"""

import os
#os.getcwd()
import tweepy
import json
import requests

#opens and reads keys.json
keys={}
with open("keys/keys.json") as file:
    keys = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
#consumer_key = keys["consumer_key"]
#consumer_secret = keys["consumer_secret"]
#access_token = keys["access_token"]
#access_token_secret = keys["access_token_secret"]

# OAuth process, using the keys and tokens
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

# Store access keys in a way to send to Twitter
#api = tweepy.API(auth)

# Write out the thing we're going to tweet
#turtle = "turtle"

# Send the tweet
#api.update_status(turtle)

# Print it out in the console
#print(turtle)

#opens and reads apikey.json
apikey={}
with open("keys/apikey.json") as file:
    apikey = json.loads(file.read())

#authenticate and calls api
x_api_key = apikey["x_api_key"]   
url = 'https://api.propublica.org/congress/v1/house/votes/recent.json'
headers = {'X-API-KEY': x_api_key}
response = requests.get(url, headers=headers)
print(response.status_code)

#status codes    
#https://www.dataquest.io/blog/python-api-tutorial/