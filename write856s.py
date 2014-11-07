#!/usr/bin/env python
"""
write out a MARC file of records with multiple 856 fields
"""
from pymarc import MARCReader, MARCWriter


reader = MARCReader( open( 'ebooks.MRC' ), to_unicode=True, force_utf8=True, utf8_handling='ignore' )
writer = MARCWriter( file( 'Two856s.MRC', 'w' ) )
limit = 200000
i = 0

for rec in reader:
    if i < limit:
        i += 1
        if rec[ '856' ] is not None:
            all856s = rec.get_fields( '856' )
            if len( all856s ) > 1:
                writer.write( rec )

writer.close()
