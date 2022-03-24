from turtle import Screen
import tweepy
import configparser
import pandas as pd 

# read config 

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication 
auth = tweepy.OAuthHandler(api_key,
    api_key_secret)
auth.set_access_token(access_token,
    access_token_secret)

api = tweepy.API(auth)

# NFT hastags

keywords = ['#NFT','#Crypto']

for i in keywords:
    limit = 5000
    tweets = tweepy.Cursor(api.search_tweets,
    q = keywords, count = 50,tweet_mode='extended').items(limit)


# create DataFrame

columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

df.to_csv("NFT.csv")