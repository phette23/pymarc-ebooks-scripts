#!/usr/bin/env python
""" output CSV of record titles that have multiple 856 fields """
from pymarc import MARCReader
import csv


reader = MARCReader(open('TEST.MRC'))
csvfile = open('Test-dual856s.csv', 'w')
csvwriter = csv.writer(csvfile)
all856s = []
limit = 100000
i = 0

# header row
csvwriter.writerow(['Title', '1st 856', '2nd 856'])

for rec in reader:
    if i < limit:
        i += 1
        row = []
        if rec['856'] is not None:
            all856s = rec.get_fields('856')
            if len(all856s) > 1:
                row.append(rec.title())
                for f in all856s:
                    row.append(f.value())
                csvwriter.writerow(row)

csvfile.close()
