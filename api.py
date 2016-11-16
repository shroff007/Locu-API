
import urllib2
import json

locu_api = 'Your API Key'

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
