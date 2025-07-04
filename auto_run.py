'''
Retrieve and update the UNL JSON periodically.
Write the results to a .json file.
'''

import time
import json
import logging

from parse_unl import unl_parser

UNL_URL = "https://vl.xahau.org"
#UNL_URL = "https://vl.ripple.com"

TIME_PAUSE = 900 #Time in seconds to wait between queries.
OUTPUT_FILE = "./unl_mappings.json"
LOG_FILE = "./unl_parser_auto.log"
LOG_LEVEL = logging.INFO

def start_log():
    '''
    Configure logging.
    '''
    logging.basicConfig(
            filename=LOG_FILE,
            level=LOG_LEVEL,
            datefmt="%Y-%m-%d %H:%M:%S",
            format='%(asctime)s %(levelname)s: %(module)s - %(funcName)s (%(lineno)d): %(message)s',
            )
    logging.info("Logging configured.")

def write_out(unl):
    if unl['error'] is False and unl['http_code'] == 200:
        with open(OUTPUT_FILE, "w+") as output:
            output.write(json.dumps(unl))
        logging.info(f"Wrote UNL with: {unl['validator_count']} items.")
    else:
        logging.Warning(f"Error retrieving UNL: {unl}")

def run():
    start_log()
    n = 1
    while True:
        try:
            unl = unl_parser(UNL_URL)
            write_out(json.loads(unl))
            print("UNL tool running for the", n, "iteration.")
            n+=1
            time.sleep(TIME_PAUSE)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run()
