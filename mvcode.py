#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:33:32 2018

@author: gmkaniku
"""

import tweepy
import json
import requests
import pandas as pd
import numpy as np


#opens and reads mvkey.json
mvkey={}
with open("keys/mvkey.json") as file:
    mvkey = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
consumer_key = mvkey["consumer_key"]
consumer_secret = mvkey["consumer_secret"]
access_token = mvkey["access_token"]
access_token_secret = mvkey["access_token_secret"]

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Store access keys in a way to send to Twitter
api = tweepy.API(auth)

# Write out the thing we're going to tweet
def buildTweet(argument1, argument2, argument3):
    tweet = argument1 + " missed a vote on " + argument2 + ". " + argument3
#    tweet = argument1 + ", " + argument2 + ", " + " missed a vote because of '" + argument3 + "'. " + argument4   
#    tweet = "On " + argument1 + " " + argument2 + " said '" + argument3 + ".'"
    sendTweet(tweet)       

# Send the tweet
def sendTweet(content):
    api.update_status(content)
#    except tweepy.error.TweepError:
#        pass



#opens and reads apikey.json
apikey={}
with open("keys/apikey.json") as file:
    apikey = json.loads(file.read())
#authenticate and calls api to print text
x_api_key = apikey["x_api_key"]

#calls senate members api and puts results into json
urlsenate = 'https://api.propublica.org/congress/v1/115/senate/members.json'
headers = {'X-API-KEY': x_api_key}
responsesenate = requests.get(urlsenate, headers=headers)
jsonfilesenate = responsesenate.json()

#json data in senate results into dataframe
datasenate = jsonfilesenate.get('results')
for s in datasenate:
    membersenate = s['members']
    membersenate_df = pd.DataFrame(membersenate)

#find senate member ids for MD members
membersenate_df = membersenate_df.replace(np.nan, '', regex=True)
maryland = membersenate_df[membersenate_df['state'].str.contains("MD")]

#put only MD senate member ids in array
arrayid = []
if (len(maryland)) > 0:
    mrowid = maryland.iterrows()
    for m in mrowid:
        arrayid.append(m[1]['id'])
        
        
#calls house members api and puts results into json
urlhouse = 'https://api.propublica.org/congress/v1/115/house/members.json'
responsehouse = requests.get(urlhouse, headers=headers)
jsonfilehouse = responsehouse.json()

#json data in house results into dataframe
datahouse = jsonfilehouse.get('results')
for h in datahouse:
    memberhouse = h['members']
    memberhouse_df = pd.DataFrame(memberhouse)

#find house member ids for MD members
memberhouse_df = memberhouse_df.replace(np.nan, '', regex=True)
maryland = memberhouse_df[memberhouse_df['state'].str.contains("MD")]
     
#put only MD house member ids in array
if (len(maryland)) > 0:
    mrowid = maryland.iterrows()
    for m in mrowid:
        arrayid.append(m[1]['id'])   



#takes out each member id out of the array 1 at a time
for memid in arrayid:

    #calls excuses for all legislative MD members api and puts results in json
    urlexcuse = 'https://api.propublica.org/congress/v1/members/' + memid + '/explanations/115.json'
    responseexcuse = requests.get(urlexcuse, headers=headers)
    jsonfileexcuse = responseexcuse.json()
    
    #if MD member has no excuses removes their results
    dataexcuse = jsonfileexcuse.get('results')
    if len(dataexcuse) == 0:
        continue
    else:
        #if MD member has excuses gets name and info on excuses and tweets 
        mdexcuse_df = pd.DataFrame(jsonfileexcuse)
        if (len(mdexcuse_df) > 0):
            irow = mdexcuse_df.iterrows()
            for m in irow:
                print(m[1]['display_name'])
    
        dataexcuse_df = pd.DataFrame(dataexcuse)
        if (len(dataexcuse_df) > 0):
            irow = dataexcuse_df.iterrows()
            for i in irow:
                print(i[1]['date'])
                print(i[1]['url'])
#                buildTweet(m[1]['display_name'],i[1]['date'],i[1]['url'])       


#https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions

                

    


