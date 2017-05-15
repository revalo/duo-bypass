import pyotp
import requests
import base64
import json
import sys
from urllib2 import unquote

if len(sys.argv) < 2:
    print "Usage: python duo_bypass.py <url to duo qr>"; exit()

qr_url = sys.argv[1]
data = unquote(qr_url.split('=')[1])

hostb64 = data.split('-')[1]

host = base64.b64decode(hostb64 + '='*(-len(hostb64) % 4))
code = data.split('-')[0].replace('duo://', '')

url = 'https://{host}/push/v2/activation/{code}'.format(host=host, code=code)
r = requests.post(url)
response = json.loads(r.text)

secret = base64.b32encode(response['response']['hotp_secret'])

print "10 Next OneTime Passwords!"
# Generate 10 Otps!
hotp = pyotp.HOTP(secret)
for _ in xrange(10):
    print hotp.at(_)
