Simple program that allows you to send an sms to your Twilio number and receive carbon output data for your zip code's
power grid from [WattTime](http://www.watttime.org).

Requires the geopy, twilio, requests, and json python libraries, a WattTime API token, Flask, and a [Twilio](https://www.twilio.com) account.
    
Simply run on your internet-facing server and paste yoururl:5000 into the sms field of your Twilio number.
Currently only accepts five-digit integers, all other inputs and null responses generate "Sorry, no data found."
