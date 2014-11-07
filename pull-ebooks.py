#!/usr/bin/env python
"""
write all the records with 856 fields out to an ebooks-only MARC file
"""
from pymarc import MARCReader, MARCWriter

"""
the MARCReader params come from the penultimate comment here:
github.com/edsu/pymarc/issues/7
basically, these work around mixed character encodings
"""
allRecords = MARCReader( open( 'ebooks.MRC' ), to_unicode=True, force_utf8=True, utf8_handling='ignore' )
onlyEbooks = MARCWriter( file( 'ebooks-edited.MRC', 'w' ) )

errCount = 0

for rec in allRecords:
    if rec[ '856' ] is not None:
        try:
            onlyEbooks.write( rec )
        except UnicodeDecodeError:
            print rec[ '245' ]
            errCount += 1

print "\nNumber of Errors: ", errCount

onlyEbooks.close()
