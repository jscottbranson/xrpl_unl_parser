'''
Retrieve and parse a published rippled UNL
'''

import json
from hashlib import sha256
from base64 import b64decode
import requests


def base58_encode(key):
    '''
    Returns a string that is encoded using the rippled base58 alphabet.
    '''
    alphabet = b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'
    string = b""
    while key:
        key, idx = divmod(key, 58)
        string = alphabet[idx:idx+1] + string
    return string

def parser(address):
    '''
    Download the UNL and base64 decode the blob.
    '''
    validation_keys = []
    validators = json.loads(b64decode(
        json.loads(requests.get(address).content)['blob']))['validators']
    for i in validators:
        payload = "1C" + i['validation_public_key']
        hash1 = sha256(bytearray.fromhex(payload)).hexdigest()
        checksum = sha256(bytearray.fromhex(hash1)).hexdigest()[0:8]
        validation_keys.append(base58_encode(int(payload + checksum, 16)).decode('utf-8'))

    return validation_keys
