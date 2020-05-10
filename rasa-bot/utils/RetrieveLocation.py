import requests
import xml.etree.ElementTree as ET
from difflib import get_close_matches

class RetrieveLocation :

    url = "https://www.mastercard.us/locator/NearestLocationsService/" 
    querystring = {"latitude":"18.5679146","longitude":"73.91434319999999", 
        "radius":"5","distanceUnit":"","locationType":"atm","maxLocations":"100", 
        "MERCH_ATTR_1":"","instName":"","supportEMV":"","customAttr1":"","locatonTypeId":""}
    payload = ""
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    }

    @classmethod
    def requestData(cls) :
        return requests.request("GET", cls.url, data = cls.payload, headers = cls.headers, params = cls.querystring)

    @classmethod
    def parseXML(cls, string) :
        return ET.fromstring(string)

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
    def getAddress(cls, data, toFind) :

        allAddress = [] 
        userLocation = toFind['location'].upper()

        for location in data :

            address = cls.__store_values(location)

            if toFind['postalCode'] and address['postalCode'] :
                if toFind['postalCode'] == address['postalCode'] :
                    address = list(address.values())
                    address = list(filter(None, address))
                    allAddress.append(address)
                    continue

            for key in address :
                if address[key] and address[key].find(userLocation) != -1 :
                    address = list(address.values())
                    address = list(filter(None, address))
                    allAddress.append(address)
                    break

        if allAddress :
            return allAddress
        
        for location in data :

            address = cls.__store_values(location)
            address = list(address.values())
            address = list(filter(None, address))

            matches = get_close_matches(userLocation, address, cutoff=0.6)
            if matches :
                allAddress.append(matches)

        return allAddress