import re
import io
import csv
import tweepy
from tweepy import OAuthHandler
import tweepy as tw
import array as arr
import Config
import SendData
from io import StringIO 

import os
from dotenv import load_dotenv

load_dotenv()

consumer_secret = os.getenv('consumer_secret')
consumer_key = os.getenv('consumer_key')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')


# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

def create_sms(sms_body):
    SendData.send_sms(sms_body)

def get_tweets():
    
    # Define user ids 
    
    user_ids = {
    "thatMRFBat" : "1095283958",
    "amazonIndia" : "1282946089",
    "flipkart" : "57947109",
    "croma" : "54516116",
    "sony_india" : "43845681",
    "reliance" : "146371658",
    "Consoles_India":"1438818407592316930",
    "icgoriginal":"1389191128713338885"
    }
                                                                                
    word_list = ['PS5', 'PlayStation','Play Station', 'Play Station 5','Play station']
    
    #create an array
    for index in user_ids.values():

        # call twitter api to fetch tweets
        fetched_tweets = tw.Cursor(api.user_timeline,
                   user_id=index,
                   count=20,                                  
                   exclude_replies = True,
                   include_rts=False).items(5)

        stringBuilder = StringIO()
    
        for tww in fetched_tweets:
            if any(word in tww.text for word in word_list):
                print(tww._json['user']['screen_name'])
                stringBuilder.write("PS5 News from "+tww._json['user']['screen_name'+"\n"])
                stringBuilder.write(tww._json['entities']['urls'][0]['expanded_url']+"\n")
                stringBuilder.write(tww._json['created_at'])
                create_sms(stringBuilder.getvalue())   
        

    # calling function to get tweets
get_tweets()

