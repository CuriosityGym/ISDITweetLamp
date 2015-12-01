import time
import serial
from twython import Twython


TWITTER_APP_KEY = ''                #Insert your consumer key here
TWITTER_APP_KEY_SECRET = ''         #Insert your consumer secret here
TWITTER_ACCESS_TOKEN = ''           #Insert your access token here
TOKEN_SECRET = ''                   #Insert your access token secret here

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flush()

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TOKEN_SECRET)

hashtag = ''                        #Insert the hashtag you want to track

search = t.search(q=hashtag, count=1)

while True:
  search = t.search(q=hashtag, count=1)
  tweets = search['statuses']
  for tweet in tweets:
    if 'red' in tweet['text']:
      ser.write('a')
    if 'green' in tweet['text']:
      ser.write('b')
    if 'blue' in tweet['text']:
      ser.write('c')
    if 'yellow' in tweet['text']:
      ser.write('d')
    if 'orange' in tweet['text']:
      ser.write('e')
    if 'violet' in tweet['text']:
      ser.write('f')
    if 'rainbow' in tweet['text']:
      ser.write('g')
    if 'ripple' in tweet['text']:
      ser.write('h')
    print tweet['text'], '\n\n\n'
  time.sleep(3)
