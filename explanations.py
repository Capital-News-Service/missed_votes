import json
import tweepy

#opens and read json file
keys={}
with open("json/keys.json") as file:
    keys = json.loads(file.read())
    keys={}
    
# Consumer keys and access tokens, used for OAuth
consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

#Twitter tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
turtle = "turtle"
api.update_status(turtle)

print(turtle)
