#!/usr/python3

from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

from geopy.geocoders import Nominatim

watttime_token = 'Token '
headers = {'Authorization': watttime_token}


def parse_mix(carbon, timestamp):
    carbon_rounded = round(carbon, 3)
    day = timestamp[0:10]
    time = timestamp[11:16]
    text_string = "%s lbs/kwh at %sUTC on %s" % (carbon_rounded, time, day)
    return text_string


def parse_text(text):
    # Parses text into a zip code or rejects.
    if len(text) == 5 and text.isdigit():
        zip = text
    else:
        zip = False
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
    if resultsjson:
        abbrev = resultsjson[0]['abbrev']
        return abbrev
    else:
        return False


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
        return False


def text_data(mix_string):
    # Texts the mix data out via Twilio
    if mix_string:
        text_text = mix_string
    else:
        text_text = "Sorry, no data found"
    return text_text


def do_it(text):
    message = text_data(get_mix_data(loc_to_ba(zip_lookup(parse_text(text)))))
    return message


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    body = request.values.get('Body')
    text_message = do_it(body)
    resp = twilio.twiml.Response()
    resp.message(text_message)
    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
