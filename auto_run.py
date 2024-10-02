'''
Retrieve and update the UNL JSON periodically.
Write the results to a .json file.
'''

import time
import json

from parse_unl import unl_parser

UNL_URL = "https://vl.xahau.org"
#UNL_URL = "https://vl.xrplf.org"
#UNL_URL = "https://vl.ripple.com"

OUTPUT_FILE = "./unl_mappings.json"
TIME_PAUSE = 120 #Time in seconds to wait between queries.

def write_out(unl):
    if unl:
        with open(OUTPUT_FILE, "w+") as output:
            output.write(unl)

def run():
    n = 1
    while True:
        try:
            unl = unl_parser(UNL_URL)
            write_out(unl)
            print("UNL tool running for the", n, "iteration.")
            n+=1
            time.sleep(TIME_PAUSE)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run()
