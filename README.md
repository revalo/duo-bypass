## Duo One Time Password Generator

This is a little script I put together after I reverse engineered the Duo 2FA Mobile App and figured out how their auth flow works. This can be ported into probably a useful desktop app or chrome extention and can probably be used to write bots for MIT Services that require auth.

### Usage

Install stuff,

```
pip install -r requirements.txt
```

Just grab the QR Code URL that starts with `duo://` and execute,

```
python duo_bypass.py duo://urlhere
```

### How does this work?

It's pretty simple so I won't explain. The hard part was to read DUO's obfuscated code, because obfuscation makes things so secure.

Why didn't I sniff? Because HTTPS and because they apparantly ignore trusted CA's on the Android Device and also the fact that I was too lazy to get a USB cable from my room and also that I didn't want to download a gigabyte of emulator.

When I almost got all of it I realized I could have probably decompiled their Windows app, coz .NET and and coz they didn't obfuscate that. rip me.

Anyway, it's 9 AM and I should sleep.