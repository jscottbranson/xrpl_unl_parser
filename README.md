# xrpl_unl_parser
This library retrieves and parses published Unique Node Lists (UNLs), such as the Xahau UNL published at "https://vl.xahau.org" or the XRP Ledger UNL published at `https://vl.xrplf.org`. It consists of two functions - one to retrieve and parse the UNL, and the second to encode the resultant public validation keys using rippled's base58 alphabet.

A JSON object that includes a dictionary of  base58 encoded public validation keys with their domain mappings is returned.

## Required Packages
* `pip install requests base58 cryptography ecpy`

* `git clone https://github.com/antIggl/xrpl-unl-manager.git && mv xrpl-unl-manager ./xrpl_unl_manager`

## Use
This has been tested in Python versions 3.5, 3.6, and 3.7. Feedback on testing with earlier versions is appreciated.
```
from parse_unl import unl_parser

ADDRESS = "https://vl.ripple.com"
KEYS = unl_parser(ADDRESS)
```

A JSON object is returned with the following keys:
- `status`: Either `Error` or `Success`.
- `error`: `False` if no error, or error details.
- `http_code`: Returns the http code as an integer, if it is available.
- `publisher_key`: The public key used to sign the published UNL.
- `validator_count`: The number of validators in the UNL.
- `mappings`: Returns a dictionary of parsed keys with domains, or an empty dict if an error is encountered.
- `expiration`: UNL expiration date (Unix Epoch).

## Limitations and Future Development
The script does not verify the signature for the UNL manifest. Hopefully this will be available in a future version.

## Known Validator List Sites
- `https://vl.xahau.org`
- `https://vl.xrplf.org`
- `https://vl.ripple.com`


## License
GNU GPLv3

## Contact
Visit me at [https://rabbitkick.club] or on Twitter [@jscottbranson].

## Thanks
Special thanks to [Alloy] for his invaluable input and assistance testing!

Thanks to [Antonios Inglezakis] for his UNL tool.


[Alloy]:https://twitter.com/alloynetworks
[Antonios Inglezakis]:https://github.com/antIggl
