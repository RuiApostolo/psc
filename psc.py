#!/usr/bin/env python
from collections import Counter

# Proline       P = 0
# Aspartic Acid D = 2
# Glutamic Acid E = 2
# B and Z ?
# U ?
# X special case - counted separately
# J, O doens't exist
# * translation stop
# - gap
# All others      = 1
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '*', '-'
]

c = Counter()


f = open("P69905.fasta", 'r')
lines = iter(f)
# Skip first line. - change to check first character
next(f)
for line in lines:
    c.update(line)

# Remove carriage return symbol
c['\n'] = 0
# print(list(c.elements()))
# Print frequency list
print("Frequency list:")
for i in alphabet:
    print(i, c[i])

c += Counter()

b = True
for i, j in c.items():
    if i not in alphabet:
        if b is True:
            print("Wrong symbols list:")
            b = False
        print(i, c[i])
