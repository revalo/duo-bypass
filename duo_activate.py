#!/usr/bin/env python3
import pyotp
import requests
import base64
import json
import sys
from Crypto.PublicKey import RSA

raw_input: str = sys.argv[1]
split_raw_input: list = raw_input.split('-')
code: str = split_raw_input[0]
encoded_host: str = split_raw_input[1]
host: str = base64.decodebytes(encoded_host.encode('utf-8') + b'==').decode()

# Obsolete documentation for reference purposes:
#The QR Code is in the format: XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
#copy 'XXXXXXXXXX' to "code"
#use https://www.base64decode.org/ to decode YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY and put it in 'host'
#decoded format should be in the format: api-XXXXX.duosecurity.com
#host = 'api-XXXXX.duosecurity.com'
#code = 'XXXXXXXXXX'

url = 'https://{host}/push/v2/activation/{code}?customer_protocol=1'.format(host=host, code=code)
headers = {'User-Agent': 'okhttp/2.7.5'}
data = {'pkpush': 'rsa-sha512',
        'pubkey': RSA.generate(2048).public_key().export_key("PEM").decode(),
        'jailbroken': 'false',
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

with open('duotoken.hotp', 'w') as file:
    file.write(secret.decode() + "\n")
    file.write("0")

with open('response.json', 'w') as resp:
    resp.write(r.text)
