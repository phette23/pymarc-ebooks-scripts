#! /usr/bin/env python
"""
output stats on 856 subfield usage
"""
from pymarc import MARCReader

"""
Notes:
856 = web access
$x = nonpublic note
$u = link URL
$z = public note

LOC Definition: www.loc.gov/marc/bibliographic/bd856.html
"""

reader = MARCReader(open('MARC/2013-12-13-full-catalog.MRC'))
numWith856x = 0
numWith856z = 0
num856 = 0

for record in reader:
    if record['856'] is not None:
        num856 += 1
        if record['856']['x'] is not None:
            numWith856x += 1
        if record['856']['z'] is not None:
            numWith856z += 1

print "Number with 856:", num856
print "Number with 856 $x:", numWith856x
print "Number with 856 $z:", numWith856z
