from time import sleep
from os import system
import requests
import random
import sys


def iplookup(IP):
        url = 'http://ip-api.com/json/{}'.format(IP)
        response = requests.get(url)
        geoip = response.json()
        
        asn = geoip["as"]
        city = geoip["city"]
        country = geoip["country"]
        countrycode = geoip["countryCode"]
        isp = geoip["isp"]
        lat = geoip["lat"]
        lon = geoip["lon"]
        org = geoip["org"]
        query = geoip["query"]
        region = geoip["region"]
        regionname = geoip["regionName"]
        status = geoip["status"]
        timezone = geoip["timezone"]
        zip = geoip["zip"]
        
        print ("IP Info For: {}".format(IP))
        print ("IP address: {}".format(query))
        print ("as: {}".format(asn))
        print ("city: {}".format(city))
        print ("country: {}".format(country))
        print ("country code: {}".format(countrycode))
        print ("isp: {}".format(isp))
        print ("lat: {}".format(lat))
        print ("lon: {}".format(lon))
        print ("org: {}".format(org))
        print ("region: {}".format(region))
        print ("region name: {}".format(regionname))
        print ("timezone: {}".format(timezone))
        input("press enter to exit")


print("Enter the website url you want to get details for")
ip = input("Enter URL: ")
iplookup(ip)
