#!/usr/bin/env python
"""
output a CSV of all ebook record titles & (first) 856$u field
usage: ./ebooks-to-csv.py > output.csv
"""

from pymarc import MARCReader

ebooks = MARCReader(open('ebooks-edited.MRC'),
                    to_unicode=True, force_utf8=True, utf8_handling='ignore')

# limit output, for quicker testing
# 200000 = unlimited, because we don't have that many items
limit = 200000
i = 0

# CSV header line
print "Title, URL"

for rec in ebooks:
    if i < limit:

        if rec['856'] is not None:
            # cache lookup
            f856 = rec['856']

            if f856['u'] is not None:
                print '"' + rec.title() + '", "' + f856['u'] + '"'
        i += 1
