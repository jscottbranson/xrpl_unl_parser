'''
Compare two UNLs.
'''
import json
from parse_unl import unl_parser

XRPLF = unl_parser("https://vl.xrplf.org")
Ripple = unl_parser("https://vl.ripple.com")
Coil = unl_parser("https://vl.coil.com")

XRPLF = json.loads(XRPLF)['public_validation_keys']
Ripple = json.loads(Ripple)['public_validation_keys']
Coil = json.loads(Coil)['public_validation_keys']

difference = list(set(Coil) - set(Ripple) - set(XRPLF))

print(f"Difference: {difference}.")
