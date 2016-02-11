import twilio
import requests
import json


def receive_text(text):
    # Receives and parses text into a zip code.
    zip = ""
    return zip


def zip_lookup(zip):
    # Take zip code and find coords.
    long = ""
    lat = ""
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
