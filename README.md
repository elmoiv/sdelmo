# sdelmo
[![Build Status](https://api.travis-ci.org/elmoiv/sdelmo.svg?branch=master)](https://travis-ci.org/elmoiv/sdelmo)
[![Python version](https://img.shields.io/badge/python-3.6-blue.svg)](https://pypi.org/project/sdelmo/)

Simple Soundcloud music downloader.

## Features
* Download any public soundcloud audio file.
* audio files can be downloaded with cover if you have [eyeD3](https://eyed3.readthedocs.io/).

## Installation
`sdelmo` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install sdelmo
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/elmoiv/sdelmo.git
```

## Usage
```
import sdelmo

sdelmo.scdl(client_id, track_url)
```

## How to get `client_id` (in case of expiry)

You can find client_id by searching through XHR requests:

![alt text](https://i.imgur.com/Xl3JnuP.png)

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/sdelmo/issues) or send me a pull request.
