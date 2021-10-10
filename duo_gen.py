#!/usr/bin/env python3

import pyotp
import sys

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = "duotoken.hotp"

f = open(file, "r+");
secret = f.readline()[0:-1]
offset = f.tell()
count = int(f.readline())

print("secret", secret)
print("count", count)

hotp = pyotp.HOTP(secret)
print("Code:", hotp.at(count))

f.seek(offset)
f.write(str(count + 1))
f.close()
