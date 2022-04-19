## Duo One Time Password Generator

This is a little script I put together after I reverse engineered the Duo 2FA
Mobile App and figured out how their auth flow works. This can be ported into
probably a useful desktop app or chrome extention and can probably be used to
write bots for MIT Services that require auth.

### Usage

Install stuff,

```
pip install -r requirements.txt
```

Copy the QR code image (or create a screenshot) and store it as qr.png into this folder.

Then run:
```
./duo_activate.py
```

In case the QR code cannot be decoded automatically, you will be asked for its text value, it is the format:  
XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

The displayed code is the XXXXXXXXXX part of the QR code.  
The displayed host is the base64 decoded YYYYYY[...] part of the QR code.
It should be in the format: api-XXXXX.duosecurity.com.

If everything worked you can then generate a code by running:

```
./duo_gen.py
```

Warning: These are HOTP tokens and generate codes increments a counter.  If you
get too far out of sync with the server it will stop accepting your codes.

```
./duo_export.py
```

Export the duo hotp secret as a QR code for inclusion in third-party hotp apps
like freeotp.
