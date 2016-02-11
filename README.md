Simple program that allows you to send an sms to your Twilio number and receive carbon output data for your zip code's
power grid from WattTime.org.

Requires:
    Python libraries:
        twilio
        geopy
        requests
        json
    
    And a Twilio account.
    
Simply run on your internet-facing server and paste yoururl:5000 into the sms field of your Twilio number.
Currently only accepts five-digit integers, all other inputs and null responses generate "Sorry, no data found."