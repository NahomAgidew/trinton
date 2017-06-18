"""
Gets tweets from twitter,
Runs a sentiment analysis,
and predicts the winner of the U.S. 2016 election.

@author Nahom Abi
"""

#twitter API
import tweepy
#sentiment analysis library
from textblob import TextBlob

#get these from https://apps.twitter.com/
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

#initializing twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

clinton_polarity = []
trump_polarity = []


def analyze(tweet_text, person):
    if(person == "Clinton"):
        analysis = TextBlob(tweet_text)
        clinton_polarity.append(analysis.sentiment[0])
    elif(person == "Trump"):
        analysis = TextBlob(tweet_text)
        trump_polarity.append(analysis.sentiment[0])


def main():
    print "Getting tweets..."
    for i in ["Clinton", "Trump"]:
        for tweet in api.search(i):
            analyze(tweet.text, i)

    cl_avg, tr_avg = sum(clinton_polarity)/len(clinton_polarity), sum(trump_polarity)/len(trump_polarity)
    if cl_avg > tr_avg:
        print "As of now, Hillary Clinton will win!"
    elif tr_avg > cl_avg:
        print "As of now, Donald Trump will win!"
    else:
        print "Tie :("


if __name__ == '__main__':
    main()
