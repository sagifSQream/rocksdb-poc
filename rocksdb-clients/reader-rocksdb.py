import base64
from typing import Dict, List

import requests

url = 'http://localhost:4080/get'


def readFromDB(keys):
    enc_keys = []
    for k in keys:
        enc_keys.append(base64.b64encode(k.encode('utf-8')).decode('ascii'))


    reqBody: dict[str, str | list[str]] = {
        'name': 'sagi',
        'keys': enc_keys
    }
    resp = requests.post(url, json=reqBody)
    if not resp.ok:
        print('failed to save keys: {0}'.format(resp.json()))


    values=resp.json()['body']
    for i in range(len(values)):
        if not values[i]:
            raise Exception('value of index {0} was null'.format(i))


key_val = 0
while key_val == 0:
    keys = []

    for k in range(100000):
        key_val += 1
        keys.append('k_{0}'.format(key_val))
    try:
        readFromDB(keys=keys)
        print('Read keys from {0} ok'.format(key_val))
    except Exception as ex:
        print('Failed to write key. communication error', ex)
