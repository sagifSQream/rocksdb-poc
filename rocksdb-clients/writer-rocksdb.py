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


def writeToDB(keys, values,startIndex):
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

    print("starting to write bulk keys from {0}".format(startIndex))
    resp = requests.post(url, json=reqBody)
    if not resp.ok:
        print('failed to save keys: ', resp.json())
    else:
        print('wrote {0} keys from index {1}'.format(len(keys),startIndex))

key_val = 0
range_size = 100000
while True:
    keys = []
    values = []
    for k in range(range_size):
        key_val += 1
        keys.append('k_{0}'.format(key_val))
        values.append('v_{0}_{1}'.format(key_val,time.time_ns()))

    try:
        writeToDB(keys=keys, values=values,startIndex=key_val)
        key_val=0  # restart writing
    except Exception as ex:
        print('Failed to write key from {0}. error:{1}'.format(range_size, ex))
        key_val -= range_size
        time.sleep(5)
        exit (0)

    