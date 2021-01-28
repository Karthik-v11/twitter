import tweepy
#import os

#consumer_key=os.getenv('consumer_key')
#consumer_secret=os.getenv('consumer_secret')
#access_token=os.getenv('access_token')
#access_token_secret=os.getenv('access_token_secret')

#auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#auth.set_access_token(access_token,access_token_secret)
CONSUMER_KEY='23qtZgYoYQHA8yTuE2jymBkma'
CONSUMER_SECRET='50pQUQPDwI5Yvv4Cfi9bav9MTfNRQaVoiXvNglLp31Y27hZYSO'
ACCESS_TOKEN='1135552582259159040-fa59BslRG7uIe3p81ceSF6bZXgNyi2'
ACCESS_TOKEN_SECRET='pqwWZfn358uPdhL69tWsca467zzDk4H9sPiwsxKKITEaI'

auth= tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)

import time

while True:
  user=api.get_user('_karthik_V_')
  n=user.followers_count
  api.update_profile(name=f'Karthik {n} followers')
  print(f'Karthik {n} followers')
  time.sleep(60)
