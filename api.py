
import urllib2
import json

locu_api = 'c23822c852b5a7102e7c9dab77e6852a68e54c61'

def locu_search(query2):
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + locu_api
    #locality = query1.replace(' ', '%20')
    region = query2.replace(' ', '%20')
    final_url = url + "&region=" + region + "&category=restaurant"

    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    for item in data['objects']:
        print item['name'], item['phone']

locu_search('arizona')