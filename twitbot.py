import tweepy
import json
from textblob import TextBlob
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='twits',
                             port=8889,
                             cursorclass=pymysql.cursors.DictCursor)

print("Setting Up Tweepy Api ...")

consumer_key="UgkTh5rjU0WL1jVx2OA4c4Oyq"
consumer_secret="vQ8H5B2ctITTIwBKWV2Rr97i5toJKVzp4Awrr6IEQXq2RCvDHG"
access_token="784225248493367296-BTQE4PhHdoHm5pKLAc9zpDrEawF07C3"
access_token_secret="MgLuTsH7rTBK2fChZ7oX11h7RdWEf7ElywuvqPXsd47n9"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


print("Searching Tweets ...")
print

sentiment=[]

for tweet in tweepy.Cursor(api.search, q="BancodelSol", tweet_mode="extended").items(10):
    twitEs=TextBlob(tweet.full_text)
    twitEn=twitEs.translate(to="en")
    sentiment.append({twitEn.sentiment.polarity, twitEn.sentiment.subjectivity, tweet.full_text})
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO `bancoDelSol` (`subjectivity`, `polarity`, `text`) VALUES (%s, %s, %s)", (twitEn.sentiment.subjectivity, twitEn.sentiment.polarity, json.dumps(tweet.full_text)))



connection.commit()
 




    