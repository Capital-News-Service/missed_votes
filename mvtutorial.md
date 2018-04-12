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
  - Import json
  - Call in authentication information from keys.json
  - Store them so they can be passed into Twitter

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
  - Import Tweepy
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
* Turn dictionary into data frame
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
* Use requests.get to call URL for "lists of members" for senate
* Headers for authenticating xapikey
* Get json file as dictionary
* Turn only the column members into a dataframe
* Search dataframe for "state=MD" 
* Iterating over rows that are MD and take out member ids
* Put members ids in separate array

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
 ```
 * Repeat process for "lists of members" for house
 * Put MD members ids in same array
 ```       
        
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

#### Version 5
Take out each member id and pass it into excuse api
* Make a for loop saying for each member id in the array id
* Pass the id into the url of "get recent personal explanations by a specific member"
* Get a dictionary

```
for memid in arrayid:

    #calls excuses for all legislative MD members api and puts results in json
    urlexcuse = 'https://api.propublica.org/congress/v1/members/' + memid + '/explanations/115.json'
    responseexcuse = requests.get(urlexcuse, headers=headers)
    jsonfileexcuse = responseexcuse.json()
```

#### Version 6
Take out members with no excuses
* Take the results column from the dictionary and put it in a list
* See if there are any columns in the list that are empty
* Pass over those columns

```
    #if MD member has no excuses removes their results
    dataexcuse = jsonfileexcuse.get('results')
    if len(dataexcuse) == 0:
        continue
```

#### Version 7
* Turn dictionay of specific member excuses into a dataframe
* Iterate over rows to get the name and print out
* Turn the results section of the dictionary into a seperate dataframe
* Iterate over the rows to get the date and url to print out
* Send name, date, and url arguments to buildTweet

```
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
                buildTweet(m[1]['display_name'],i[1]['date'],i[1]['url'])  
```

#### Version 8
Make a tweet to send out
* Update the buildTweet function to import 3 arguments
* Create a sentence of what you want to tweet out using the arguments
* Send the sentence to the sendTweet function
* Use a tweepy method to update Twitter status with the tweet

```
# Write out the thing we're going to tweet
def buildTweet(argument1, argument2, argument3):
    tweet = argument1 + " missed a vote on " + argument2 + ". " + argument3
    sendTweet(tweet)       

# Send the tweet
def sendTweet(content):
    api.update_status(content)
``` 




