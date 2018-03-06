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
* Create GitHub repo with 4 files - mvkey.json, readme.md, GitIgnore, & explanations.py
* Write the following code in mvkey.json:
  - consumer key, consumer key secret, access token, & access token secret
* Write the following code in explanations.py:
  - Import Tweepy
  - Call in authentication information from keys.json
  - Store them so they can be passed into Twitter
  - Create keyword to tweet out
  - Tweet out keyword with authentication to test
```
import tweepy

mvkey={}
with open("keys/mvkey.json") as file:
    mvkey = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
consumer_key = mvkey["consumer_key"]
consumer_secret = mvkey["consumer_secret"]
access_token = mvkey["access_token"]
access_token_secret = mvkey["access_token_secret"]
```
  - Create keyword to tweet out
  - Tweet out keyword with authentication
  
```
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Store access keys in a way to send to Twitter
api = tweepy.API(auth)

# Write out the thing we're going to tweet
def buildTweet(argument1):
    print("missed votes")
    sendTweet(tweet)

# Send the tweet
def sendTweet(content):
    try:
        api.update_status(content)
    except tweepy.error.TweepError:
        pass
```

#### Version 2 
Print out in console the 20 most recent explanations of all members of Congress as json
* Get ProPublica Congress API key
* Store in apikey.json file
* Call in authentication information from apikey.json
* Import requests
* Use requests.get to call URL for "get recent personal explanations"
* Headers for authenticating xapikey
* Print json as string in console to test

```
import requests

#opens and reads apikey.json
apikey={}
with open("keys/apikey.json") as file:
    apikey = json.loads(file.read())
#authenticate and calls api to print text
x_api_key = apikey["x_api_key"]

#calls explanations api and puts results into json
url = 'https://api.propublica.org/congress/v1/115/explanations.json'
headers = {'X-API-KEY': x_api_key}
response = requests.get(url, headers=headers)
jsonfile = response.json()
```

#### Version 3
Print out in console the 20 most recent explanations of all members of Congress formatted as tweets then tweet them out
* Turn json string into data frame
* Search object for arguments by iterating over rows
* Send arguments to buildTweet to tweet out

```
#json data in senate results into dataframe
data = jsonfile.get('results')
for s in data:
    member = s['results']
    member_df = pd.DataFrame(member)
    
#find MD members
member_df = senate_df.replace(np.nan, '', regex=True)
maryland = member_df[member_df['state'].str.contains("MD")]

#put only MD member ids in array
arrayid = []
if (len(maryland)) > 0:
    mrowid = maryland.iterrows()
    for m in mrowid:
        print(m[1]['id'])
        buildTweet(m[1]['id'])
```
		
#### Version 4
Get all of the member ids from all members of Congress from MD from the House and Senate

```
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
```

#### Version 6
Take member ids and send them to the excuses API to get all excuses from MD members

```
for memid in arrayid:

    #calls excuses for all legislative MD members api and puts results in json
    urlexcuse = 'https://api.propublica.org/congress/v1/members/' + memid + '/explanations/115.json'
    responseexcuse = requests.get(urlexcuse, headers=headers)
    jsonfileexcuse = responseexcuse.json()
```


#### Version 7
If a MD member has no excuses remove their results

```
    dataexcuse = jsonfileexcuse.get('results')
    if len(dataexcuse) == 0:
        continue
```

#### Version 8



https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-access-metrics.html
https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html




