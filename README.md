# xrpl_unl_parser
This library retrieves and parses published Unique Node Lists (UNLs), such as the UNL published at `https://vl.ripple.com`. It consists of two functions - one to retrieve and parse the UNL, and the second to encode the resultant public validation keys using rippled's base58 alphabet.

A JSON object that includes a list of  base58 encoded public validation keys is returned.

## Required Packages
`requests` - Used to retrieve the encoded UNL

## Use
This has been tested in Python versions 3.5, 3.6, and 3.7. Feedback on testing with earlier versions is appreciated.
```
from parse_unl import unl_parser

ADDRESS = "https://vl.xrplf.org"
KEYS = unl_parser(ADDRESS)
```

A JSON object is returned with the following keys:
- `status`: Either `Error` or `Success`.
- `error`: Empty string if no error, or error details.
- `http_code`: Returns the http code as an integer, if it is available.
- `public_validation_keys`: Returns a list of parsed keys, or an empty list if an error is encountered.
- `expiration`: UNL expiration date (Unix Epoch).

## Limitations and Future Development
The script does not verify the signature for the UNL manifest. Hopefully this will be available in a future version.

## Known Validator List Sites
- `https://vl.xrplf.org`
- `https://vl.ripple.com`
- `https://vl.coil.com`


## License
GNU GPLv3

## Contact
Visit me at [https://rabbitkick.club] or on Twitter [@rabbitkickclub].

## Thanks
Special thanks to [Alloy] for his invaluable input and assistance testing!


[https://rabbitkick.club]:https://rabbitkick.club
[@rabbitkickclub]:https://twitter.com/rabbitkickclub
[Alloy]:https://twitter.com/alloynetworks
