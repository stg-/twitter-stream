# twitter-stream

**Steps to run this docker:**

#1 - Create a keys.yml file (e.g. /mydisk/keys.yml) with the following structure and add your data to it:

keys:
access_token:
access_token_secret:
consumer_key:
consumer_secret:

#2- Then run it like this:
docker run --rm -v /mydisk/keys.yml:/root/keys.yml twitter-stream

