#!/usr/bin/env python
""" print number of records with a particular MARC field tag
usage: ./count-tag.py file.mrc 856
prints something like "Number of records with 856 field = 12012" """
from pymarc import MARCReader
import sys


def usage():
    print "Usage:"
    print "\t./count-tag.py $file $tag"
    print "\te.g. ./count-tag ebooks.MRC 245"
    exit()

try:
    if sys.argv[ 1 ] == 'help' or sys.argv[ 1 ] == '--help' or sys.argv[ 1 ] == '-h':
        usage()
except IndexError:
    usage()

filename = sys.argv[ 1 ]
reader = MARCReader( open( filename ), to_unicode=True, force_utf8=True, utf8_handling='ignore' )
tag = sys.argv[ 2 ]
tagCount = 0

for record in reader:
    if record[ tag ] is not None:
        tagCount += 1

print "Number of records with ", tag, " field = ", tagCount
