import twilio
import requests
import json

from geopy.geocoders import Nominatim


watttime_token = '062fcb6e4c2eac88241e0a727f2cf4fb8c1cca29'
twilio_id = 'AC1773d28a4edb400cd3a97a854ded20e1'
twilio_token = 'fb67c60d1088d5b503b0ef1e00ab526c'


def receive_text(text):
    # Receives and parses text into a zip code.
    zip = ""
    return zip


def zip_lookup(zip):
    # Take zip code and find coords.
    geolocator = Nominatim()
    location = geolocator.geocode(zip)

    lat = location.latitude
    long = location.longitude

    return long, lat


def loc_to_ba(long, lat):
    ba = ""
    return ba


def get_mix_data(ba):
    # Takes the balancing authority and returns mix data.
    mix_data = {}
    return mix_data


def text_data(mix_data):
    # Texts the mix data out via Twilio
    pass


def text_sorry():
    pass


print(zip_lookup("27514"))