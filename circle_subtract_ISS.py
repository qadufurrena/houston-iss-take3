import json
import urllib.request
import os
import math
import tweepy as tp
from time import sleep

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['acces_token']
access_secret = environ['access_secret']

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

text = "Look to the Skies! The ISS is over Houston"

#center_lon and center_lat JSC coordinates, center_lon = -95.093186
#center_lat = 29.552839
#latitude: 1 deg = 110.574km
#longitude: 1 deg = 111.320*cos(latitude)km
#radius of visibility = 2316.4km, when=> 40deg in sky, radius = 1774.5km  
#deploy for godsake!!!

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    R = 1774.5
    center_lon = -95.093186
    center_lat = 29.552839
    x = lon
    y = lat
    Rlat = abs((center_lat-y) * 110.574)
    Rlon = abs((center_lon-x) * (111.320 * math.cos(y*0.01745329)))
    C = (math.sqrt(((Rlat) ** 2) + ((Rlon) ** 2)))
    if C <= R:
        print("It's here!", "lat:", lat, "lon:", lon, "Rlat:", Rlat, "Rlon:", Rlon, "C:", C)
        api.update_status(text)
        sleep(1800)
    else:
        print("nope", "lat:", lat, "lon:", lon, "Rlat:", Rlat, "Rlon:", Rlon, "C:", C)
        sleep(5)
    





