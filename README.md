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

Just grab the QR Code URL and copy the string after value

https://api-XXX.duosecurity.com/frame/qr?value={VALUE}

```
./duo_activate.py {VALUE}
```

If everything worked you can then generate a code by running:

```
./duo_gen.py
```

Warning: These are HOTP tokens and generate codes increments a counter.  If you 
get too far out of sync with the server it will stop accepting your codes.

