'''
Retrieve and parse a published rippled UNL.
Returns base58 encoded XRP Ledger keys.
This script relies on: https://github.com/antIggl/xrpl-unl-manager/tree/master
to parse validator manifests.
'''

import json
from hashlib import sha256
from base64 import b64decode
import requests
from xrpl_unl_manager import utils as parse_manifest

UNL_URL = "https://vl.xahau.org"
#UNL_URL = "https://vl.xrplf.org"

def rippled_bs58(key):
    '''
    Returns a string that is encoded using the rippled base58 alphabet.
    '''
    alphabet = b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'
    string = b""
    while key:
        key, idx = divmod(key, 58)
        string = alphabet[idx:idx+1] + string
    return string

def decode_pub_key(key):
    '''
    Decode public validation or list signing keys.
    '''
    payload = "1C" + key
    key_decode = rippled_bs58(int(payload + sha256(bytearray.fromhex(sha256(
            bytearray.fromhex(payload)).hexdigest())).hexdigest()[0:8], 16)).decode('utf-8')
    return key_decode

def unl_parser(url):
    '''
    Download the UNL and base64 decode the blob.
    Defaults to https://vl.ripple.com
    Individual validation keys are then constructed from the decoded blob
    payload and the double sha256 hashed checksums. Keys are then base58 encoded.
    '''
    keys = {'status': 'Error',
            'error': False,
            'http_code': '',
            'publisher_key': '',
            'validator_count': 0,
            'mappings': {},
            'expiration': '',}

    try:
        unl = requests.get(url)
        keys['http_code'] = unl.status_code
        unl.raise_for_status()
    except requests.exceptions.RequestException:
        keys['error'] = "Invalid URL: {}.".format(url)
        return json.dumps(keys)

    try:
        blob = json.loads(b64decode(unl.json()['blob']).decode('utf-8'))
        validators = blob['validators']
        '''
        Convert Ripple Epoch to Unix Epoch
        Reference : https://xrpl.org/basic-data-types.html
        '''
        keys['expiration'] = blob['expiration'] + 946684800

    except json.decoder.JSONDecodeError:
        keys['error'] = "Invalid or malformed manifest."
        return json.dumps(keys)

    if not validators:
        keys['error'] = "List of validator keys was empty."
        return json.dumps(keys)

    else:
        for i in validators:
            manifest = parse_manifest.decodeManifest(i['manifest'])
            try:
                domain = manifest['domain'].decode('utf-8')
            except KeyError:
                domain = "Domain not specified"
            keys['mappings'][
                    decode_pub_key(i['validation_public_key'])] = domain
        keys['validator_count'] = len(keys['mappings'])
        keys['publisher_key'] = decode_pub_key(unl.json()['public_key'])

    keys['status'] = 'Success'
    return json.dumps(keys)

if __name__ == "__main__":
    UNL = unl_parser(UNL_URL)
    print(UNL)
