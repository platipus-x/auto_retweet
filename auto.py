import tweepy as twitter
import constant
import time, datetime

auth = twitter.OAuthHandler(constant.CONSUMER_KEY, constant.CONSUMER_SECRET)
auth.set_access_token(constant.ACCESS_KEY, constant.ACCESS_SECRET)
api = twitter.API(auth)

#heroku deploy

def twitter_bot(username, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search, q=username, rpp=10).items(5):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                print("id: " + str(tweet_id))
                print("text: " + str(tweet_text))

                api.retweet(tweet_id)

            except twitter.TweepError as error:
                print(error.reason)


        time.sleep(3600)

twitter_bot("from:_Weeekly", 10)