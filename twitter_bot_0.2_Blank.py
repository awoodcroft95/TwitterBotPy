#!/usr/bin/env python
from twython import Twython
import time
# twitter consumer and access information goes here
apiKey= ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''

continueTweeting = True
keywordlist = "" #words used to search or remove from search

def autoBot():
	twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	search_results = twitter.search(f="twimg", q=keywordlist, count=1, lang="en") #grab one tweet using the keyword list, must be in english, must contain an image
	try: # retweet the selected tweet, favourite that tweet
		for tweet in search_results["statuses"]:
			twitter.retweet(id = tweet["id_str"])
			twitter.create_favorite(id = tweet["id_str"])
			print ("Tweeted:" + tweet["id_str"])
	except TwythonError as e:
		print (e)
	for tweet in search_results["statuses"]: #follow the account from the search
		twitter.create_friendship(id = tweet["user"]['id_str'])
		print("Followed:" + tweet["user"]['screen_name'])
	try: # follow all followers
		followers = twitter.get_followers_ids(screen_name = "") #Username goes here
		for followers_ids in followers['ids']:
			twitter.create_friendship(user_id=followers_ids)
	except TwythonError as e:
		print(e)
		
while continueTweeting == True: #run the autoBot every 20 minutes 
	autoBot()
	time.sleep(1200)