# import twilio
import requests
import json

from geopy.geocoders import Nominatim

watttime_token = 'Token 062fcb6e4c2eac88241e0a727f2cf4fb8c1cca29'
headers = {'Authorization': watttime_token}
twilio_id = 'AC1773d28a4edb400cd3a97a854ded20e1'
twilio_token = 'fb67c60d1088d5b503b0ef1e00ab526c'


def parse_mix(carbon, timestamp):
    carbon = round(carbon, 3)


def receive_text(text):
    # Receives and parses text into a zip code.
    zip = ""
    return zip


def zip_lookup(zip):
    # Take zip code and find coords.
    geolocator = Nominatim()
    location = geolocator.geocode(zip)

    lat = str(location.latitude)
    lon = str(location.longitude)

    return [lon, lat]


def loc_to_ba(coords):
    url = 'https://api.watttime.org/api/v1/balancing_authorities/?loc={' \
          '"type":"Point","coordinates":[%s,%s]}' % (
              coords[0], coords[1])
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    resultsjson = json.loads(r.text)
    abbrev = resultsjson[0]['abbrev']
    return abbrev


def get_mix_data(ba):
    # Takes the balancing authority and returns mix data.
    url = "https://api.watttime.org:443/api/v1/datapoints/?ba=%s" % ba
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    resultsjson = json.loads(r.text)
    latest = (next((x for x in resultsjson['results'] if x['carbon']), None))
    if latest:
        carbon = latest['carbon']
        timestamp = latest['timestamp']
        return parse_mix(carbon, timestamp)
    else:
        return "No data found"


def text_data(mix_data):
    # Texts the mix data out via Twilio
    pass


def text_sorry():
    pass


print(get_mix_data("ISONE"))
