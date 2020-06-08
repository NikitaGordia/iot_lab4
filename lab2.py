import urllib.parse, urllib.request, json, ssl

ssl._create_default_https_context = ssl._create_unverified_context

encoding = 'UTF-8'

access_token = '45db0c8c-23b6-3ada-b496-28d655fb8f5b'
user_id = 'b748a3e0-90d1-4aa5-bc2f-4b649bb71bb5'

headers = {
    'authorization': "Bearer " + access_token,
    'Content-Type': "application/json"
}

requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/locations/user/' + user_id + '/info'

print('\nGetting User Location Info: (' + requestUrl + ')\n')

request = urllib.request.Request(requestUrl, headers=headers)

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Location Info:', results, '\n')

headers = {'authorization': "Bearer " + access_token}

requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/capabilities/customer'

print('\nGetting User capabilities: (' + requestUrl + ')\n')

request = urllib.request.Request(requestUrl, headers=headers)

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Capabilities:', results, '\n')
