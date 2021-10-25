import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceUrl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    if api_key is not False:
        params['key'] = api_key
    url = serviceUrl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print(place_id)
