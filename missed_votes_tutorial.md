## Missed Votes

**Problem:** We want to know when delegates from MD miss votes and for what reasons. It is hard to keep track of manually and by the time it is discovered or investigated, it may not be newsworthy anymore.  
**Solution:** Build a Twitter bot to automatically send out a notification when every MD senator or house member puts out an excuse for a vote.

#### Version 1 
Sends out a tweet when the program runs to a Twitter account.
* Create a gmail account for bot
  - missedvotes@gmail.com
* Create a Twitter account using gmail account
  - @missed_votes
* Get keys for Twitter account at apps.twitter.com
* Create GitHub repo with 4 files - keys.json, readme.md, GitIgnore, & filename.py
* Write the following code in keys.json:
  - consumer key, consumer key secret, access token, & access token secret
* Write the following code in filename.py:
  - Import Tweepy
  - Call in authentication information from keys.json
  - Store them so they can be passed into Twitter
  - Create keyword to tweet out
  - Tweet out keyword with authentication
'''
import tweepy
import json

mvkey={}
with open("keys/mvkey.json") as file:
    mvkey = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
consumer_key = mvkey["consumer_key"]
consumer_secret = mvkey["consumer_secret"]
access_token = mvkey["access_token"]
access_token_secret = mvkey["access_token_secret"]
'''


#### Version 2 
Print out in console the 20 most recent explanations of all members of Congress as json
* Get ProPublica Congress API key
* Store in apikey.json file
* Call in authentication information from apikey.json
* Import requests
* Use requests.get to call URL for "get recent personal explanations"
* Headers for authenticating xapikey
* Print json as string in console

#### Version 3
Print out in console the 20 most recent explanations of all members of Congress formatted as tweets then tweet them out
* Turn json string into data frame
* Search object for arguments by iterating over rows
* Create function buildTweet to take in arguments and form them into a sentence
* Create function sendTweet to tweet out sentence if it hasn't been already tweeted
		
#### Version 4
Tweet all the most recent explanations by one member of Congress from MD

#### Version 6
Tweet out most recent by all members of Congress from MD

#### Version 7
Tweet out only new explanations by all members of Congress from MD





