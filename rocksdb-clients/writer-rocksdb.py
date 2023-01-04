import base64
import os
import time
import requests

url = None
try:
    url = os.environ['HOST']
except:
    url = 'http://localhost:4080'

if not url.startswith('http'):
    url = 'http://{0}'.format(url)

if not url.endswith('/put'):
    url = '{0}/put'.format(url)

print('writing to server {0}'.format(url))


def writeToDB(keys, values):
    enc_keys = []
    enc_values = []
    for k in keys:
        enc_keys.append(base64.b64encode(k.encode('utf-8')).decode('ascii'))

    for v in values:
        enc_values.append(base64.b64encode(v.encode('utf-8')).decode('ascii'))

    reqBody: dict[str, str | list[str]] = {
        'name': 'sagi',
        'keys': enc_keys,
        'values': enc_values
    }
    resp = requests.post(url, json=reqBody)
    if not resp.ok:
        print('failed to save keys: ', resp.json())


key_val = 0
range_size = 100000
while True:
    keys = []
    values = []
    for k in range(range_size):
        key_val += 1
        keys.append('k_{0}'.format(key_val))
        values.append('v_{0}'.format(key_val * 0.1))

    try:
        writeToDB(keys=keys, values=values)
        print('wrote keys from {0} val'.format(key_val))
    except Exception as ex:
        print('Failed to write key from {0}. error:{1}'.format(range_size, ex))
        key_val -= range_size
        time.sleep(5)
