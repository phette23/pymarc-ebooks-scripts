#!/usr/bin/env python
"""
print out titles of records with a given GMD
usage: ./search-gmd.py $GMD
"""
from pymarc import MARCReader
import sys

filename = 'MARC/2013-05-03-books.MRC'
term = sys.argv[1]
limit = 1000
count = 0

reader = MARCReader(open(filename),
                    to_unicode=True, force_utf8=True, utf8_handling='ignore')

for record in reader:
    if count >= limit:
        break
    else:
        count += 1
        if record.get_fields('245') != []:
            for gmd in record['245'].get_subfields('h'):
                if term in gmd:
                    print record.title()
