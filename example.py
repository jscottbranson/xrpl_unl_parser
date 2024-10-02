'''
Compare two UNLs.
'''
import json
from parse_unl import unl_parser

XRPLF = unl_parser("https://vl.xrplf.org")
Ripple = unl_parser("https://vl.ripple.com")

XRPLF = json.loads(XRPLF)['public_validation_keys']
Ripple = json.loads(Ripple)['public_validation_keys']

difference = list(set(Ripple) - set(XRPLF))

print(f"Difference: {difference}.")
