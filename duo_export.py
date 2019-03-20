#!/usr/bin/env python3

import pyotp
import pyqrcode
import json
import base64
import sys

file_json = "response.json"

with open('response.json', "r") as f:
  response = json.loads(f.read())['response']

with open('duotoken.hotp', "r") as f:
    counter = int(f.readlines()[1])

label = response['customer_name']
issuer = 'Duo'
# base32 encoded hotp secret, with the padding ("=") stripped.
secret = base64.b32encode(bytes(response['hotp_secret'], 'utf-8')).decode('utf-8').replace('=', '')
qrdata = 'otpauth://hotp/{label}?secret={secret}&issuer={issuer}&counter={counter}'.format(label=label, secret=secret, issuer=issuer, counter=counter)
qrcode = pyqrcode.create(qrdata)
print(qrcode.terminal(quiet_zone=1))
print(qrdata)
