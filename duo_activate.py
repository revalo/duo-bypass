#!/usr/bin/env python3

import pyotp
import requests
import base64
import json
import sys

#The QR Code is in the format: XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
#copy 'XXXXXXXXXX' to "code"
#use https://www.base64decode.org/ to decode YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY and put it in 'host'
#decoded format should be in the format: api-XXXXX.duosecurity.com
host = 'api-XXXXX.duosecurity.com'
code = 'XXXXXXXXXX'

url = 'https://{host}/push/v2/activation/{code}?customer_protocol=1'.format(host=host, code=code)
headers = {'User-Agent': 'okhttp/2.7.5'}
data = {'jailbroken': 'false',
        'architecture': 'arm64',
        'region': 'US',
        'app_id': 'com.duosecurity.duomobile',
        'full_disk_encryption': 'true',
        'passcode_status': 'true',
        'platform': 'Android',
        'app_version': '3.49.0',
        'app_build_number': '323001',
        'version': '11',
        'manufacturer': 'unknown',
        'language': 'en',
        'model': 'Pixel 3a',
        'security_patch_level': '2021-02-01'}

r = requests.post(url, headers=headers, data=data)
response = json.loads(r.text)

try:
  secret = base64.b32encode(response['response']['hotp_secret'].encode())
except KeyError:
  print(response)
  sys.exit(1)

print("secret", secret)

print("10 Next OneTime Passwords!")
# Generate 10 Otps!
hotp = pyotp.HOTP(secret)
for _ in range(10):
    print(hotp.at(_))

with open('duotoken.hotp', 'w') as file
    f.write(secret.decode() + "\n")
    f.write("0")

with open('response.json', 'w') as resp:
    resp.write(r.text)
