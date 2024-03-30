## Duo One Time Password Generator

This is a little script I put together after I reverse engineered the Duo 2FA
Mobile App and figured out how their auth flow works. This can be ported into
probably a useful desktop app or chrome extention and can probably be used to
write bots for MIT Services that require auth.

### Usage

Install stuff,

```bash
pip install -r requirements.txt
```

Grab the text from the QR code, it is the format: XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

On Linux, you may use the following command that will automatically parse it from a saved qr code image.

You must save the image as `qr.png`.

```bash
sudo apt-get install zbar-tools
zbarimg qr.png | sed 's/QR-Code:duo:\/\/\(.*\)/\1/'
```

Then, replace `XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY` with your text, and run:

```bash
./duo_activate.py XXXXXXXXXX-YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

If everything worked you can then generate a code by running:

```bash
./duo_gen.py
```

Warning: These are HOTP tokens and generate codes increments a counter.  If you
get too far out of sync with the server it will stop accepting your codes.

```bash
./duo_export.py
```

Export the duo hotp secret as a QR code for inclusion in third-party hotp apps
like freeotp.
