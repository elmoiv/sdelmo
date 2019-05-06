#       sdelmo.py, simple Souncloud music downloader.
#
#       Copyright 2019 Khaled El-Morshedy <elmoiv>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the attached License.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import requests, json, urllib.request, os
from lxml import html
from tqdm import tqdm

# Technique from https://github.com/tqdm/tqdm#hooks-and-callbacks
class Pgbr(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def Filter(txt):
    for i in r'<>:"/\|?*':
        txt = txt.replace(i, ' - ')
    return txt

def scdl(client_id, url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    trackId = tree.xpath('/html/head/meta[30]/@content')[0].split(':')[-1]
    trackTitle = tree.xpath('/html/head/meta[23]/@content')[0]
    trackCover = tree.xpath('/html/head/meta[28]/@content')[0]
    api = json.loads(requests.get(f'https://api.soundcloud.com/i1/tracks/{trackId}/streams?client_id={client_id}').content)
    trackUrl = api['http_mp3_128_url']
    with Pgbr(unit='B', unit_scale=True, miniters=1, desc=trackTitle[:13] + '...') as t:
        urllib.request.urlretrieve(trackUrl, filename='$.mp3', reporthook=t.update_to)
    try:
        import eyed3
        print('Furnishing...\n')
        mp3 = eyed3.load('$.mp3')
        if mp3.tag == None:
            mp3.initTag()
        mp3.tag.images.set(3, requests.get(trackCover).content, 'image/jpeg')
        mp3.tag.save()
    except ImportError:
        print('eyeD3 module is not installed! Songs will be saved without album cover :(')
    except:
        print('Unexpected Error!')
    os.rename('$.mp3', f'{Filter(trackTitle)}.mp3')
    
