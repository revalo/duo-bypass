#!/usr/bin/env python2.7

import pyotp
import requests
import base64
import json
import sys
from urllib2 import unquote

if len(sys.argv) < 2:
    print "Usage: python duo_bypass.py <url to duo qr>"; exit()

qr_url = sys.argv[1]
data = qr_url #unquote(qr_url.split('=')[1])

hostb64 = data.split('-')[1]

print "hostb64", hostb64

host = base64.b64decode(hostb64 + '='*(-len(hostb64) % 4))
code = data.split('-')[0]

print "host", host
print "code", code

url = 'https://{host}/push/v2/activation/{code}'.format(host=host, code=code)
r = requests.post(url)
response = json.loads(r.text)

print "url", url
print "r", r
print "response", response
secret = base64.b32encode(response['response']['hotp_secret'])

print "secret", secret

print "10 Next OneTime Passwords!"
# Generate 10 Otps!
hotp = pyotp.HOTP(secret)
for _ in xrange(10):
    print hotp.at(_)

f = open('duotoken.hotp', 'w')
f.write(secret + "\n")
f.write("0")
f.close()

