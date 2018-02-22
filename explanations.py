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
import pandas as pd

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
def buildTweet(text):
    tweet = text
    print(tweet)
    #sendTweet(tweet)

# Send the tweet
#def sendTweet(content):
#    api.update_status(content)

# Print it out in the console
#print(turtle)

#opens and reads apikey.json
apikey={}
with open("keys/apikey.json") as file:
    apikey = json.loads(file.read())

#authenticate and calls api to print text
x_api_key = apikey["x_api_key"]

url = 'https://api.propublica.org/congress/v1/115/explanations.json'
headers = {'X-API-KEY': x_api_key}
response = requests.get(url, headers=headers)
jsonfile = response.json()

#data in results into dataframe
data = jsonfile['results']
data_df = pd.DataFrame(data)

#finds specific column in dataframe  
if (len(data_df) > 0):
    irow = data_df.iterrows()
    for i in irow:
        print(i[1]['member_id'])
        
#        buildTweet(i[1]['member_id'])
        
        
          




    


