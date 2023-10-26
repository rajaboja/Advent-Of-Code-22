import os
import requests
from urllib.parse import urlsplit


def get_data(url):
    fp = "data/"+ urlsplit(url).path.split('/')[-2]+'.txt'
    if not os.path.isfile(fp):
        data = requests.get(url,cookies={'session':os.environ.get('SESSION_ID')}).content
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp,'wb') as f:
            f.write(data)
    return fp