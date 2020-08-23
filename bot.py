import tweepy
import time as timer
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)

user = api.me()

d = datetime.today() - timedelta(hours=3)

def woj():
    woj_tweets = []
    for status in tweepy.Cursor(api.user_timeline, id="wojespn", tweet_mode="extended").items(100):
        if ("Atlanta" in status.full_text) or ("Atlanta's" in status.full_text) or ("Hawks" in status.full_text) or ("hawks" in status.full_text) or ("ATL" in status.full_text):
            if (status.full_text.startswith('RT')):
                continue
            if status.created_at >= d:
                woj_tweets.append(status)

    for ww in woj_tweets:
        try:
            api.update_status("https://twitter.com/wojespn/status/" + str(ww.id))
        except tweepy.TweepError:
            woj_tweets.remove(ww)
            pass


while True:    
    woj()
    timer.sleep(10800)
