import requests, json, os, sys

from lxml import html


# https://sumit-ghosh.com/articles/python-download-progress-bar/
def download(url, filename):

    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        
        else:
            downloaded = 0
            total = int(total)

            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):

                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)

                file_size = round(total / (1024**2))
                file_down = round(downloaded / (1024**2))

                sys.stdout.write('\r[{}{}] [{}/{} MB]'.format('█' * done, ' ' * (50-done), file_down, file_size))
                sys.stdout.flush()

    sys.stdout.write('\n')


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

    api = json.loads(requests.get('https://api.soundcloud.com/i1/tracks/{}/streams?client_id={}'.format(trackId, client_id)).content)
    trackUrl = api['http_mp3_128_url']
    
    # I saved it as $ to avoid unicode error for non english names after applying eyed3
    download(trackUrl, '$.mp3')

    try:
        import eyed3
        print('Adding Cover...\n')
        mp3 = eyed3.load('$.mp3')
        if mp3.tag == None:
            mp3.initTag()
        mp3.tag.images.set(3, requests.get(trackCover).content, 'image/jpeg')
        mp3.tag.save()
    except ImportError:
        print('Eyed3 module is not found! Songs will be saved without album cover :(')
    except:
        print('Unexpected Error!')
    
    os.rename('$.mp3', '{}.mp3'.format(Filter(trackTitle)))
