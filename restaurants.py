import requests
# import secrets
import smtplib
import json
import googlemaps
import time
import pandas as pd


# get the API Key
with open('secrets.json') as infile:
    keys = json.load(infile)
    gkey = keys['gkey']

# Open the google client using our key and initialize an empty datafram
gmaps = googlemaps.Client(key = gkey)
df = pd.DataFrame()

# get the places around our location, google will give up to 20 different locales
places = gmaps.places_nearby(location = '39.790876, -86.142675', radius = '40000', keyword = 'restaurant')

# Sort through the locales and send in a call to get specific fields
for place in places['results']:
    # get current ID
    my_place_id = place['place_id']
    
    # define the fields we want data for
    my_fields = ['name', 'type',  'takeout', 'adr_address', 'price_level', 'rating', 'serves_breakfast', 'serves_dinner']

    # make the call to get the locale data
    my_place = gmaps.place(place_id = my_place_id, fields = my_fields)
    
    # save the data to our DataFrame
    temp = pd.DataFrame.from_dict(my_place['result'])
    df = pd.concat([df,temp])


# pause the script so Google's server can catch up
time.sleep(3) 

# repeat the steps above to get more data
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


# save the data to a csv
outfile = 'data.csv'
df.to_csv(outfile)
