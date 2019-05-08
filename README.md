# sdelmo
Simple Soundcloud music downloader.

# Features
- Download any public soundcloud audio file.
- audio files can be downloaded with cover if you have [eyeD3](https://eyed3.readthedocs.io/).

# How to Use
```
import sdelmo

sdelmo.scdl(client_id, track_url)
```
- _client_id_ : must be a string value.
- _track_url_ : must be a string value.

# How to get client_id (in case of expiry)
You can find client_id by searching through XHR requests:
![alt text](https://i.imgur.com/Xl3JnuP.png)
