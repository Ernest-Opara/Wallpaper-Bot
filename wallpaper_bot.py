# themodelbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'cxZhHUUI0O0sP4H8UZiOpDsgL'
consumer_secret = 'KgCIIagNFmphfeclJpp4naFilE32YEdvBX1hPJDAFjSxyEofBW'
access_token = '1184954975962750976-6rKcEPbH5OwvybcdhfNLORmaYX7gcz'
access_secret = 'I6H0Eke3uwM39ojHsFwaImsDhzXuhtlYvJLi3uvTtsETy'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('Images')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(5)
