import requests
import xml.etree.ElementTree as ET
from difflib import get_close_matches
from geopy.geocoders import Nominatim

ATM_URL = "https://www.mastercard.us/locator/NearestLocationsService/"
ATM_PARAM = {
    "latitude" : "",
    "longitude" : "",
    "radius" : "5",
    "distanceUnit" : "",
    "locationType" : "atm",
    "maxLocations" : "100"
}

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

        if (cls.__setLatitudeAndLongitude(location)) :
            return requests.request("GET", cls.atm_url, params = cls.atm_param)
        else :
            return None

    @classmethod
    def parseXML(cls, string) :

        return ET.fromstring(string)

    @classmethod
    def getAddress(cls, data, toFind) :

        allAddress = []
        # userLocation = toFind['location'].upper()

        # # To match by pincode
        # for location in data :
        #     address = cls.__store_values(location)
        #     if toFind['postalCode'] and address['postalCode'] :
        #         if toFind['postalCode'] == address['postalCode'] :
        #             address = list(address.values())
        #             address = list(filter(None, address))
        #             allAddress.append(address)
        #             continue

        # if allAddress :
        #     return allAddress

        # # To match by location name as substring
        # for location in data :
        #     address = cls.__store_values(location)
        #     for key in address :
        #         if address[key] and address[key].find(userLocation) != -1 :
        #             address = list(address.values())
        #             address = list(filter(None, address))
        #             allAddress.append(address)
        #             break

        # if allAddress :
        #     return allAddress

        # # To match by location name which is somewhat similar to original location
        # # Also for handling minor mistakes in spellings
        # for location in data :
        #     address = cls.__store_values(location)
        #     address = list(address.values())
        #     address = list(filter(None, address))

        #     matches = get_close_matches(userLocation, address, cutoff=0.6)
        #     if matches :
        #         allAddress.append(address)

        # if allAddress :
        #     return allAddress

        # Return all locations retrieved
        for location in data :
            address = cls.__store_values(location)
            address = list(address.values())
            address = list(filter(None, address))
            allAddress.append(address)

        return allAddress
