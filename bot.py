import tweepy
import time as timer
from html.parser import HTMLParser
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler('C733a1oBB5Ug9vty4XNDSFjTj', 'eaOE3Ao0RvIc2XPq2sTczc5TDCc0auqxVqCIktwI2bQUCTnQ4a')
auth.set_access_token('1296946162256289796-2n1NiyiVw0lkxwVqyMoLSH4BEy7Smf', 'rtgMck21eVgoeXvfMLVkASHA73DgjSglkyWWqfmfAUESy')
api = tweepy.API(auth)

user = api.me()

# print(user.screen_name)

d = datetime.today() - timedelta(hours=3)

def woj():
    woj_tweets = []
    for status in tweepy.Cursor(api.user_timeline, id="wojespn", tweet_mode="extended").items(100):
        if ("Spurs" in status.full_text) or ("Atlanta's" in status.full_text) or ("Hawks" in status.full_text) or ("hawks" in status.full_text):
            if ("@" in status.full_text):
                continue
            if status.created_at >= d:
                woj_tweets.append(status)

    for ww in woj_tweets:
        # w = ww.full_text
        # print(w)
        try:
            api.update_status("https://twitter.com/wojespn/status/" + str(ww.id))
        except tweepy.TweepError:
            woj_tweets.remove(ww)
            pass


    # functions to run
woj()

    # testers for now, will remove after a beta deploy period
    # c += 1
    # api.update_status("TESTING HEROKU" + str(c))

    # # wake up to potentially tweet only once every 3 hours
    # timer.sleep(10800)