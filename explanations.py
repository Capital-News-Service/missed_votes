import tweepy
import requests
import datetime
import pandas as pd
import numpy as np
import json
import pycurl

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
