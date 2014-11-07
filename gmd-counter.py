#!/usr/bin/env python
"""
count occurrences of GMD field in collection of MARC records
see gmds-example.json for sample of what it outputs
"""
from pymarc import MARCReader

filename = 'MARC/2013-12-13-full-catalog.MRC'

limit = 500000
total = 0
count = 0
gmds = {
    "book": 0,
    "computer file": 0,
    "sound recording": 0,
    "videorecording": 0,
    "electronic": 0
}

reader = MARCReader(open(filename),
                    to_unicode=True, force_utf8=True, utf8_handling='ignore')


# increment count for given gmd
def add(gmd):
    global gmds
    gmd = gmd.encode('ascii', 'ignore')

    for material in gmds:
        if material in gmd:
            gmds[material] += 1
            return

    if gmd in gmds:
        gmds[gmd] += 1
        return
    else:
        gmds[gmd] = 1


for record in reader:
    total += 1
    if count >= limit:
        break
    else:
        count += 1
        # some records (camcorders?) don't have a title
        if record.get_fields('245') != []:
            if len(record['245'].get_subfields('h')) == 0:
            # no GMD, assume book
                add("book")
            else:
                for gmd in record['245'].get_subfields('h'):
                    add(gmd)

print "Total: ", total
print gmds
