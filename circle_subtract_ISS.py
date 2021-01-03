import json
import urllib.request
import os
import math
import tweepy as tp
from time import sleep

consumer_key = 'NjqpiOUsds9wTCGD7nVleK3Qa'
consumer_secret = 'ER8IW1izGRqTzMz6fXnQgfb5B4lrBEqedmfgGTSZttPQLh54NT'
access_token = '1338210464669593601-yILKEId8Q5GrRm5QgrTMqoCor70Bt8'
access_secret = '2iwOwpWrvJNwL4Lwm78Ehv1ckDzpDixCZGufwvLf8tafY'

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

text = "The ISS is over Houston"

#center_lon and center_lat JSC coordinates, center_lon = -95.093186
    #center_lat = 29.552839
#latitude: 1 deg = 110.574km
#longitude: 1 deg = 111.320*cos(latitude)km
#radius of visibility = 2316.4km 

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    R = 2316.4
    center_lon = -95.093186
    center_lat = 29.552839
    Rlat = abs((center_lat-lat) * 110.574)
    Rlon = abs((center_lon-lon) * (111.320 * math.cos(lat)))
    while Rlat > R or Rlon > R:
        print("nope")
        sleep(5)
    else:
        api.update_status(text)
        print("It's here!")
        sleep(1800)
        





