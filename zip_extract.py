# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from geopy.geocoders import GoogleV3
geocoder = GoogleV3()

location = geocoder.geocode("1600 Pennsylvania Ave NW, Washington, DC")
address = location.raw["address_components"]
print(address)

for item in address:
	if item["types"][0] == "postal_code":
		postal = item["long_name"]
	else:
		postal = "NA"
		
print(postal)
