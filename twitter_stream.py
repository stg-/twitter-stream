#!/usr/bin/python                                                                           

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import yaml
import os.path

if not os.path.isfile('/root/keys.yml'):
    print "File /root/keys.yml doesn't exists. Please use -v to pass it to the container."
    exit()

# User credentials to access Twitter API
with open('/root/keys.yml', 'r') as f:
    doc = yaml.load(f)

access_token = doc["keys"]["access_token"]
access_token_secret = doc["keys"]["access_token_secret"]
consumer_key = doc["keys"]["consumer_key"]
consumer_secret = doc["keys"]["consumer_secret"]

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
