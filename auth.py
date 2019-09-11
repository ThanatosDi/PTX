import datetime
import hmac
import time
from base64 import b64encode

import requests

class RequestError(Exception):
    pass


class Auth():
    '''PTX authentication  
    
    '''
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
    
    def signature(self, xdate):
        HMAC = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), 'sha1').digest()
        return b64encode(HMAC).decode()

    def request(self, endpoint, params, **kwargs):
        api = 'https://ptx.transportdata.tw/MOTC'
        xdate = time.strftime("%a, %d %b %Y %I:%M:%S GMT", time.gmtime())
        signature = self.signature(xdate)
        headers = {
            'Authorization': f'hmac username="{self.app_id}", algorithm="hmac-sha1", headers="x-date", signature="{signature}"',
            'x-date': xdate,
            'Accept-Encoding': 'gzip, deflate'
        }
        with requests.get(f'{api}{endpoint}', headers=headers, params=params, **kwargs) as req:
            if req.status_code != 200:
                raise RequestError(f'請求錯誤 {req.status_code}')
            return req.content