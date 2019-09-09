# sdelmo
Simple Soundcloud music downloader.

## Features
* Download any public soundcloud audio file.
* audio files can be downloaded with cover if you have [eyeD3](https://eyed3.readthedocs.io/).

## Usage
```
import sdelmo

sdelmo.scdl(client_id, track_url)
```
- _client_id_ : must be a string value.
- _track_url_ : must be a string value.

## How to get client_id (in case of expiry)

You can find client_id by searching through XHR requests:

![alt text](https://i.imgur.com/Xl3JnuP.png)

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/sdelmo/issues) or send me a pull request.
