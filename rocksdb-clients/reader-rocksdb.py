import base64
import time
import requests
import os

url = None
try:
    url = os.environ['HOST']
except:
    url = 'http://localhost:4080'

if not url.startswith('http'):
    url = 'http://{0}'.format(url)

if not url.endswith('/get'):
    url = '{0}/get'.format(url)

print('reading from server {0}'.format(url))


def readFromDB(keys):
    enc_keys = []
    for k in keys:
        enc_keys.append(base64.b64encode(k.encode('utf-8')).decode('ascii'))

    reqBody: dict[str, str | list[str]] = {
        'name': 'sagi',
        'keys': enc_keys
    }
    resp = requests.post(url, json=reqBody, timeout=60)
    if not resp.ok:
        print('failed to read keys: {0}'.format(resp.json()))

    values = resp.json()['body']
    for i in range(len(values)):
        if not values[i]:
            raise Exception('value of index {0} was null'.format(i))


key_val = 0
while True:
    keys = []

    for k in range(100000):
        key_val += 1
        keys.append('k_{0}'.format(key_val))
    try:
        readFromDB(keys=keys)
        print('Read keys from {0} ok'.format(key_val))
    except Exception as ex:
        print('Failed to read keys from index {0}'.format(key_val), ex)
        key_val = 0
        time.sleep(5)
