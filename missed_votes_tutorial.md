## Missed Votes

**Problem:** We want to know when delegates from MD miss votes and for what reasons. It is hard to keep track of manually and by the time it is discovered or investigated, it may not be newsworthy anymore.  
**Solution:** Build a Twitter bot to automatically send out a notification when every MD senator or house member puts out an excuse for a vote.

#### Version 1 
Sends out a tweet when the program runs to a Twitter account.
* Create a gmail account for bot
* Create a Twitter account using gmail account
* Get keys for Twitter account at apps.twitter.com
* Create GitHub repo with 4 files - keys.json, readme.md, GitIgnore, & filename.py
* Write the following code in keys.json:
  - Add consumer key, consumer key secret, access token, & access token secret
* Write the following code in filename.py:
  - Import Tweepy
  - Call in authentication information from keys.json
  - Store them so they can be passed into Twitter
  - Create keyword to tweet out
  - Tweet out keyword with authentication




