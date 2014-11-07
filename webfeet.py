#!/usr/bin/env python
"""
outputs number of these terrible "Web Feet" records we had in our catalog
because we wanted to delete them all
"""
from pymarc import MARCReader

reader = MARCReader(open('ebooks.MRC'))
numWF = 0
op = ''

for record in reader:
    op = ''
    if record['245'] is not None:
        if record['245']['c'] is not None:
            if record['245']['c'] == '[selected by Web Feet].':
                numWF += 1
                print record.title()

print "Web Feet records: ", numWF
