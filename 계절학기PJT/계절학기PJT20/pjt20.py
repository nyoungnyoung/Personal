import requests
import json

nextUrl = 'alpha'
URL = 'http://13.125.222.176/quiz/' + nextUrl
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
data = json.dumps({'nickname': '구미2반윤선영', 'yourAnswer': 'hellossafy'})

r = requests.post(URL, headers=headers, data=data)
print(r.json())


