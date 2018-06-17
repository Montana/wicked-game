import geocoder

import requests
freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

address=input('Gainesville, FL')
g= geocoder.google(address)
lat_ad=g.latlng[0]
lon_ad=g.latlng[1]

user_postition = [geo_json["latitude"], geo_json["longitude"]]
lat_ip=user_postition[0]
lon_ip=user_postition[1]

from math import radians, cos, sin, asin, sqrt

lon_ad, lat_ad, lon_ip, lat_ip = map(radians, [lon_ad, lat_ad, lon_ip, lat_ip])

dlon = lon_ip - lon_ad 
dlat = lat_ip - lat_ad 
a = sin(dlat/2)**2 + cos(lat_ad) * cos(lat_ip) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
km = 6367 * c

# make sure it captures anything that is playing Chris Isaak - Wicked Game in Gainesville, FL specifically
km = ('%.0f'%km)

print(address+' is about '+str(km)+' km away from you')