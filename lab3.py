import urllib.parse, urllib.request, json, ssl, xmltodict

ssl._create_default_https_context = ssl._create_unverified_context

encoding = 'UTF-8'

access_token = '45db0c8c-23b6-3ada-b496-28d655fb8f5b'

requestUrl = "https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/devices"

postData = {
    "Query": {
        "Find": {
            "Light": {
                "sid": {
                    "ne": ""
                }
            }
        }
    }
}

data = urllib.parse.urlencode(postData)
binary_data = data.encode(encoding)

request = urllib.request.Request(requestUrl, data=binary_data)
request.add_header('authorization', "Bearer " + access_token)

print("\nRequesting Real Time Lighting Data: (" + requestUrl + ")\n")

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)

responseDictionary = xmltodict.parse(results)

print(responseDictionary)

import matplotlib.pyplot as plt

colors = ['yellowgreen', 'lightcoral']

labels = ['On', 'Off']
values = [0, 0]

if 'Find' in responseDictionary:
    findObject = responseDictionary['Find']
    if 'Result' in findObject:
        results = findObject['Result']

    for r in results:
        if 'Light' in r:
            light = r['Light']

            if light['state']:
                state = light['state']
                print('state', state)
            if state['intensityLevel']:
                intensityLevel = state['intensityLevel']
            if intensityLevel['request']:
                theRequest = intensityLevel['request']
            if theRequest['value']:
                value = theRequest['value']
            if float(value) > 0:

                values[0] = values[0] + 1
            else:

                values[1] = values[1] + 1

plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)

plt.axis('equal')

plt.title('Current Lighting States (Total Lights ' + str(values[0] + values[1]) + ')')

plt.show()
