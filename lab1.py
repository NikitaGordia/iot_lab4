import urllib.parse, urllib.request, json, ssl

ssl._create_default_https_context = ssl._create_unverified_context

loginUrl = 'https://ckcsandbox.cisco.com/corev4/token'

headers = {
    'Cache-Control': "no-cache",
    'Content-Type': "application/x-www-form-urlencoded",
    'Postman-Token': "2915798c-f468-407c-a2dd-8897e441102b"
}

postData = {
    'client_secret': 'nOZd6gw9_ORlJcZkgRifzMB6nzQa',
    'client_id': 'Bpw8qejWXVQur3n6YAdqQAYtd94a',
    'grant_type': 'password',
    'username': 'nikita.gor@devnet.com',
    'password': '9seveVEGpG\\&6?TW'
}

data = urllib.parse.urlencode(postData)

encoding = 'UTF-8'

binary_data = data.encode(encoding)

print('\nLogging in:' + loginUrl + '\n')

request = urllib.request.Request(loginUrl, binary_data)
response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)
access_token = responseDictionary['access_token']
print('Response:', responseDictionary)

headers = {
    'authorization': "Bearer " + access_token,
    'Content-Type': "application/json"
}

requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/accounts/user/login'

print('\nGetting User Details: (' + requestUrl + ')\n')

request = urllib.request.Request(requestUrl, headers=headers)

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

user_id = responseDictionary['id']

print('User Details:', results, '\n')

print('These items will be used in Lesson-2:')
print('Your Access Token:', access_token)
print('Your User ID:', user_id)