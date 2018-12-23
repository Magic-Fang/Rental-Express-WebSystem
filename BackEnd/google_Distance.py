import json
import requests

def getDistance(start , end):
    API_Key = # fill in your API key

    Mode = ['walking','bicycling','driving']

    for i in range(3):
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+start+'&destination='+end+'&mode='+Mode[i]+'&key='+API_Key

        connect = requests.get(url)
        content= connect.json() #store json file

        walk_distance = ""
        walk_duration = ""
        bicycl_distance = ""
        bicycl_duration = ""
        drive_distance = ""
        drive_duration = ""

        if len(content['routes']):
            if i==0 :
                walk_distance = content['routes'][0]['legs'][0]['distance']['text']
                walk_duration = content['routes'][0]['legs'][0]['duration']['text']
            elif i==1:
                bicycl_distance = content['routes'][0]['legs'][0]['distance']['text']
                bicycl_duration = content['routes'][0]['legs'][0]['duration']['text']
            else:
                drive_distance = content['routes'][0]['legs'][0]['distance']['text']
                drive_duration = content['routes'][0]['legs'][0]['duration']['text']

        info = {'walk_distance':walk_distance,
                'walk_duration':walk_duration,
                'bicycl_distance':bicycl_distance,
                'bicycl_duration':bicycl_duration,
                'drive_distance':drive_distance,
                'drive_duration':drive_duration}
    return(info)

#print( json.dumps(content, indent=4, sort_keys=True) )
