import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")


print(getCountry("50.78.253.58"))

# {
#   "ip": "50.78.253.58",
#   "country_code": "US",
#   "country_name": "United States",
#   "region_code": "MA",
#   "region_name": "Massachusetts",
#   "city": "Boston",
#   "zip_code": "02116",
#   "time_zone": "America/New_York",
#   "latitude": 42.3496,
#   "longitude": -71.0746,
#   "metro_code": 506
# }