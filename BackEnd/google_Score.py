import json
import requests

def getScore(location):
    API_Key = # fill in your API key

    loc_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+location+'&key='+API_Key
    loc_connect = requests.get(loc_url)
    loc_content = loc_connect.json() #store json file

    if len(loc_content['results']):
        place_id = loc_content['results'][0]['place_id']
        lat = loc_content['results'][0]['geometry']['location']['lat']
        lng = loc_content['results'][0]['geometry']['location']['lng']

        url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&key='+API_Key
        connect = requests.get(url)
        content = connect.json()
        if 'rating' not in content['result']:
            content['result']['rating'] = ""
        rate = content['result']['rating']

        info = {
            'rating': rate,
            'latitude': lat,
            'longitude': lng
        }
    else:
        info = {
            'rating': "",
            'latitude': "",
            'longitude': ""
        }
    return(info)
