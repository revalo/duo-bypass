#!/usr/bin/env python2.7

import pyotp
import requests
import base64
import json
import sys
from urllib2 import unquote

f = open("duotoken.hotp","r+");
secret = f.readline()[0:-1]
offset = f.tell()
count = int(f.readline())

print "secret", secret
print "count", count

hotp = pyotp.HOTP(secret)
print "Code:", hotp.at(count)

f.seek(offset)
f.write(str(count + 1))
f.close()

