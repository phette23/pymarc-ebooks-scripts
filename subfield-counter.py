#!/usr/bin/env python
from pymarc import MARCReader
import json
import sys

filename = 'MARC/2013-05-03-books.MRC'
reader = MARCReader( open( filename ), to_unicode=True, force_utf8=True, utf8_handling='ignore' )
output = { 'records': 0 }
limit = 10


def ininc( dict, key ):
  # initializes dict.key.num as 1 if not present
  # increments if present
  if dict.get( key, 0 ) > 0:
    dict[ key ][ 'num' ] += 1
  else:
    dict[ key ] = { 'num': 1 }


def countField( field ):
  ininc( output, field.tag )


def countSubs( field ):
  try:
    for sub in field.subfields:
      ininc( output[ field.tag ], sub.tag )
  except AttributeError:
    return


def processRec( record ):
  output[ 'records' ] += 1
  for field in record.get_fields():
      countField( field )
      countSubs( field )


for record in reader:
  if output[ 'records' ] < limit:
    processRec( record )
  else:
    print json.dumps( output )
    sys.exit()
