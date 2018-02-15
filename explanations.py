#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:33:32 2018

@author: gmkanik
"""
#import needed packages
import tweepy
import json

#opens and reads json file
keys={}
with open("json/keys.json") as file:
    keys = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Store access keys in a way to send to Twitter
api = tweepy.API(auth)

# Write out the thing we're going to tweet
turtle = "turtle"

# Send the tweet
api.update_status(turtle)

# Print it out in the console
print(turtle)