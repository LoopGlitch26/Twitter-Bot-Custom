import tweepy as twitter # Basically that's all you need to pip install
import secrets
import datetime
import time

auth = twitter.OAuthHandler(secrets.API_KEY,secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN,secrets.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def bot(hashtags):
    while True: # Infinite Loop
        print(datetime.datetime.now()) # Print the date time
        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search, q = hashtag, rpp = 10).items(5): # Fetch queries as hashtags
                try:
                    id = dict(tweet._json)['id']
                    text = dict(tweet._json)['text']
                    api.retweet(id)
                    api.create_favorite(id)
                    print("Tweet ID:", id)
                    print("Tweet Text:", text)
                except twitter.TweepError as e:
                    print(e.reason)
        time.sleep(10) # To avoid spam

bot([''])    # List the hashtags to be liked and retweeted