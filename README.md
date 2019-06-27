# xrpl_unl_parser
This library retrieves and parses published Unique Node Lists (UNLs), such as the UNL published at `https://vl.ripple.com`. It consists of two functions - one to retrieve and parse the UNL, and the second to encode the resultant public validation keys using rippled's base58 alphabet.

A list of base58 encoded public validation keys is returned.

## Required Packages
`requests` - Used to retrieve the encoded UNL

## Use
```
from parse_unl import parser

address = "https://vl.ripple.com"
KEYS = parser(address)
```

The library returns a list of public validation keys.

## License
Do what ye please with this including using, modifying, and distributing it.

## Contact
Visit me at [https://rabbitkick.club] or on Twitter [@rabbitkickclub].


[https://rabbitkick.club]:https://rabbitkick.club
[@rabbitkickclub]:https://twitter.com/rabbitkickclub
