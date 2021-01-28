import tweepy
import os

consumer_key=os.getenv('consumer_key')
consumer_secret=os.getenv('consumer_secret')
access_token=os.getenv('access_token')
access_token_secret=os.getenv('access_token_secret')

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
print("everythings looks fine")

import time
while True:
  user=api.get_user('_karthik_V_')
  n=user.following_count
  api.update_profile(name=f'karthik {n} following')
  print(f'karthik{n}following')
  time.sleep(60)
  
  
  
