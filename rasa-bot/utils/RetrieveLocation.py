import requests
import xml.etree.ElementTree as ET
from difflib import get_close_matches
from geopy.geocoders import Nominatim

## Important parameters for retrieving atm locations
ATM_URL = "https://www.mastercard.us/locator/NearestLocationsService/"
ATM_PARAM = {
    "latitude" : "",
    "longitude" : "",
    "radius" : "5",
    "distanceUnit" : "",
    "locationType" : "atm",
    "maxLocations" : "10"
}

## Important parameters for latitude-longitude values
GEOCODE_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
GEOCODE_PARAM = {
    "input" : "",
    "inputtype" : "textquery",
    "fields" : "geometry",
    "key" : "AIzaSyCjAeKZrarKj4-EX5fR0iYEo-aOzU-AiGk"
}

class RetrieveLocation :

    atm_url = ATM_URL
    atm_param = ATM_PARAM
    geocode_url = GEOCODE_URL
    geocode_param = GEOCODE_PARAM

    @classmethod
    def __setLatitudeAndLongitude(cls, location) :

        try :
            # geolocator = Nominatim(user_agent = 'RasaChatBot')
            # geocode = geolocator.geocode(location)
            # cls.atm_param['latitude'] = str(geocode.latitude)
            # cls.atm_param['longitude'] = str(geocode.longitude)
            cls.geocode_param['input'] = location
            requested_data = requests.get(cls.geocode_url, params=cls.geocode_param).json()
            results = requested_data['candidates']
            location = results[0]['geometry']['location']
            cls.atm_param['latitude'] = str(location['lat'])
            cls.atm_param['longitude'] = str(location['lng'])
            return 1
        except :
            return 0

    @staticmethod
    def __store_values(location) :

        # Get the address sub-values from the parsed xml and store in dictionary
        address = {}
        address['name'] = location.find('name').text if location.find('name') is not None else None
        address['postalCode'] = location.find('address/postalCode').text if location.find('address/postalCode') is not None else None
        address['street'] = location.find('address/street').text if location.find('address/street') is not None else None
        address['city'] = location.find('address/city').text if location.find('address/city') is not None else None
        address['countrySubDivision'] = location.find('address/countrySubDivision').text if location.find('address/countrySubDivision') is not None else None
        address['country'] = location.find('address/country').text if location.find('address/country') is not None else None

        return address

    @classmethod
    def requestData(cls, location) :

        # Find and set the lat-long values in the parameter of geocoding api url
        if (cls.__setLatitudeAndLongitude(location)) :
            # Request the atm data
            return requests.request("GET", cls.atm_url, params = cls.atm_param)
        else :
            return None

    @classmethod
    def parseXML(cls, string) :

        # parse the string into xml
        return ET.fromstring(string)

    @classmethod
    def getAddress(cls, data) :

        allAddress = []

        # Return all locations retrieved
        for location in data :
            address = cls.__store_values(location)
            address = list(address.values())
            address = list(filter(None, address))
            allAddress.append(address)

        return allAddress
