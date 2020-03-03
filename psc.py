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

values = {'A': 1,
          'B': 1,
          'C': 1,
          'D': 2,
          'E': 2,
          'F': 1,
          'G': 1,
          'H': 1,
          'I': 1,
          'J': 1,
          'K': 1,
          'L': 1,
          'M': 1,
          'N': 1,
          'O': 1,
          'P': 0,
          'Q': 1,
          'R': 1,
          'S': 1,
          'T': 1,
          'U': 1,
          'V': 1,
          'W': 1,
          'X': 0,
          'Y': 1,
          'Z': 1,
          '*': 0,
          '-': 0
          }

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
print('')

c += Counter()

b = True
for i, j in c.items():
    if i not in alphabet:
        if b is True:
            print("Wrong symbols list:")
            print('')
            b = False
        print(i, c[i])

t = 0
for i, j in c.items():
    if i is 'X':
        print('Special case, X can be anythin. Counts of X = ', c[i])
    t += c[i] * values[i]

print('Total number of possible side-chains is: ', t)
print('')
