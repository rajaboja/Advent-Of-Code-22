import os
import requests
from urllib.parse import urlsplit


def get_data(url):
    fp = "data/"+ urlsplit(url).path.split('/')[-2]+'.txt'
    session_id = os.environ.get('SESSION_ID')
    if not os.path.isfile(fp):
        if not session_id:
            raise KeyError('session_id not found') 
        data = requests.get(url,cookies={'session':session_id}).content
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp,'wb') as f:
            f.write(data)
    return fp