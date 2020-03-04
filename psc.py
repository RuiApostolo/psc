#!/usr/bin/env python
from collections import Counter
import sys,argparse

# Proline       P = 0
# Aspartic Acid D = 2
# Glutamic Acid E = 2
# B and Z ?
# U ?
# X special case - counted separately
# J, O doesn't exist
# * translation stop
# - gap
# All others      = 1

# List of accepted characters
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '*', '-'
]

# Values attributed to each character
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

# Define arguments from command line, and generate help text
parser = argparse.ArgumentParser(description='Calculate the number of side chains in a protein from a fasta file.')
parser.add_argument('inputfile', metavar='fasta_file', type=str, help='Path to the input fasta file.')
# parser.add_argument('--output', '-o', help='Name for output file.', default='Nsidechains.txt')
# Parse arguments
args = parser.parse_args()
# Create empty counter
c = Counter()
# open file
f = open(args.inputfile, 'r')
# Separate file into lines
lines = iter(f)
# Skip first line
next(f)
# Iterate through lines and add to counter
for line in lines:
    c.update(line)
# Remove carriage return symbol
c['\n'] = 0
# Delete empty key-item pairs (carriage return)
c += Counter()
# Print frequency list
print("Frequency list:")
for i in alphabet:
    print(i, c[i])
print('')

# Check for items not in accepted list and print them
b = True
for i, j in c.items():
    if i not in alphabet:
        if b is True:
            print("Wrong symbols list:")
            print('')
            b = False
        print(i, c[i])

# Extra empy line if wrong symbols are present
if b is False:
    print('')

# Sum amount of possible side-chains
t = 0
for i, j in c.items():
    if i is 'X':
        # Print special cases (X - any AA)
        print('Special case, X can be anything. Counts of X = ', c[i])
        print('')
    t += c[i] * values[i]

print('Total number of possible side-chains is: ', t)
print('')
