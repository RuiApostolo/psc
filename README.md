# psc

This small python 3 script reads the amino-acid sequence from a fasta file and calculates the number of potential side-chains forming sites.
It assumes that proline can not form side-chains, and that Aspartic and Glutamic Acids can form two side-chains each.
By editing the 'values' dictionary, this behaviour can be modified.
The symbols for translation stop (*) and gap (-) are ignored (assumed zero side-chains) and the symbol for "any AA" (X) assumes zero side-chains, but the total of that symbol is printed separately.

Requires the modules 'Counter' and 'argparse' that come by default with any dev-python distribution.
If missing, try:
'$ pip install argparse --user'
'$ pip install Counter --user'
