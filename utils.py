import os
import requests
from urllib.parse import urlsplit


def get_data(url):
    dir_name = os.path.dirname(__file__)+"/data/"
    fp = dir_name+ urlsplit(url).path.split('/')[-2]+'.txt'

    session_id = os.getenv('SESSION_ID')
    if not os.path.isfile(fp):
        if not session_id:
            raise KeyError('session_id not found') 
        data = requests.get(url,cookies={'session':session_id}).content
        os.makedirs(dir_name, exist_ok=True)
        with open(fp,'wb') as f:
            f.write(data)
    return fp