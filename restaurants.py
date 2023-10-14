import requests
# import secrets
import smtplib
import json
import googlemaps
import time
import pandas as pd



with open('secrets.json') as infile:
    keys = json.load(infile)
    gkey = keys['gkey']

gmaps = googlemaps.Client(key = gkey)

df = pd.DataFrame()


places = gmaps.places_nearby(location = '39.790876, -86.142675', radius = '40000', keyword = 'restaurant')
for place in places['results']:
    my_place_id = place['place_id']

    my_fields = ['name', 'type',  'takeout', 'adr_address', 'price_level', 'rating', 'serves_breakfast', 'serves_dinner']

    my_place = gmaps.place(place_id = my_place_id, fields = my_fields)

    result = my_place_id
    temp = pd.DataFrame.from_dict(my_place['result'])
    df = pd.concat([df,temp])



time.sleep(3) 


places = gmaps.places_nearby(page_token = places['next_page_token'])

for place in places['results']:
    my_place_id = place['place_id']

    my_fields = ['name', 'type', 'takeout', 'adr_address', 'price_level', 'rating', 'serves_breakfast', 'serves_dinner']

    my_place = gmaps.place(place_id = my_place_id, fields = my_fields)
    temp = pd.DataFrame.from_dict(my_place['result'])
    df = pd.concat([df,temp])

time.sleep(3)


places = gmaps.places_nearby(page_token = places['next_page_token'])

for place in places['results']:
    my_place_id = place['place_id']

    my_fields = ['name', 'type', 'takeout', 'adr_address', 'price_level', 'rating', 'serves_breakfast', 'serves_dinner', 'serves_lunch']

    my_place = gmaps.place(place_id = my_place_id, fields = my_fields)
    temp = pd.DataFrame.from_dict(my_place['result'])
    df = pd.concat([df,temp])


# outfile = open('data.txt', 'w')
outfile = 'data.csv'
df.to_csv(outfile)