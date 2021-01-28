CONSUMER_KEY='ZzcJtOAlEyoCZlzmmf7MRKQp8'
CONSUMER_SECRET='bIQJmgQkD1AaVD4GDHZoCqtOhucw2NW5D4fR8J29PuRnJgjfYV'
ACCESS_TOKEN='1135552582259159040-Kw0ElFpHheHEnp8WJixAOUZubnlRin'
ACCESS_TOKEN_SECRET='x0o22q3bcEIhgDDog2T8kiTqtpA8r1YnOiTnHAKDg8wQf'

auth= tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)
print("everythings looks fine")

import time
while True:
  user=api.get_user('_karthik_V_')
  n=user.followers_count
  api.update_profile(name=f'karthik{n}followers')
  print(f'karthik{n}followers')
  time.sleep(60)
