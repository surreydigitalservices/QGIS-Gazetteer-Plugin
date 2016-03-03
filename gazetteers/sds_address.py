from json import loads
from collections import namedtuple

url = "https://address.digitalservices.surreyi.gov.uk/addresses"
headers = {
    'Authorization': 'Bearer REPLACE_ME_WITH_TOKEN'
}
params = {
    'postcode': '##searchstring##',
    'format': 'all'
}


def parseRequestResults(data, iface=None):
    json_result = loads(data)
    for item in json_result:
        if item['details']['isPostalAddress']:
            result = namedtuple('Result', ['description', 'x', 'y', 'zoom', 'epsg'])
            result.description = '%s, %s, %s %s' %(item['presentation']['street'], item['presentation']['town'], item['presentation']['area'], item['presentation']['postcode'])
            if ('property' in item['presentation'].keys()):
                result.description = '%s, %s' %(item['presentation']['property'], result.description)
            
            result.x = float(item['location']['long'])
            result.y = float(item['location']['lat'])
            result.zoom = 1250
            result.epsg = 4326
            yield result