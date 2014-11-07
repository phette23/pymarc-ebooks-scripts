#!/usr/bin/env python
"""
given MARC file:
- proxy certain vendor 856$u URLs
- delete other weird URLs that we don't need
- delete all 856$z subfields (make sense in our OPAC)

outputs to new MARC file. File paths are hardcoded in the "books"
and "processed" variables below.
"""
from pymarc import MARCReader, MARCWriter

books = MARCReader(open('MARC/2013-12-13-full-catalog.MRC'),
                   to_unicode=True, force_utf8=True, utf8_handling='ignore')
processed = MARCWriter(file('TEST.MRC', 'w'))

# limit output, for quicker testing
limit = 300000
i = 0
# initialize stat counters
num_total_books = 0
num_proxied_ebooks = 0
num_fields_removed = 0

# list of domains in 856 $u that correspond to an ebook subscription we have
subscription_domains = [
    'hdl.handle.net',  # ACLS Humanities
    'galenet.galegroup.com',  # GVRL
    'find.galengroup.com',
    'www.netlibrary.com',  # NetLibrary / EBSCO
    'www.netLibrary.com',  # case sensitive
    'search.ebscohost.com',
    'web.ebscohost.com',
    'online.statref.com',  # STAT Ref
    'ebooks.greenwood.com',  # ABC-CLIO / Greenwood
    'ebooks.abc-clio.com',
    'historyreferenceonline.abc-clio.com',
    'dx.doi.org',  # Springer
    'www.credoreference.com',  # Credo
    'ovidsp.ovid.com'  # Ovid
    ]

# weird or useless links that should be removed entirely
weird_domains = [
    'www.loc.gov/catdir/',  # LOC TOCs, bios, desc, etc.
    'lcweb.loc.gov/catdir/',
    'catdir.loc.gov/catdir/',
    'site.ebrary.com/lib/',  # we don't subscribe to ebrary, look like previews
    'www.ebrary.com',
    'www.josseybass.com',  # spam from publisher
    'www.e-streams.com',  # book reviews
    'www.nursespdr.com',  # login link
    'firstsearch.oclc.org',  # login link
    'bvbr.bib-bvb.de:8991',  # book reviews
    'lib.myilibrary.com',  # broken links
    'www.myilibrary.com',
    'fermat.nap.edu',  # one broken link
    'books.google.com',  # unneeded previews
    'public.eblib.com',  # ToCs from Ebook library
    'www.h-net.org',  # book reviews
    'library2.simpsonuniversity.edu',  # broken links
    'www.contentreserve.com',  # preview content
    'images.contentreserve.com',
    'edrev.asu.edu',  # book reviews
    'catalogimages.wiley.com'  # book cover
    ]


# update 856 $u with proxy prefix
def prefix(field):
    proxy = "http://ccproxy.idm.oclc.org/login?url="
    newU = proxy + field['u']
    field.delete_subfield('u')
    field.add_subfield('u', newU)


# delete 856 $z field
def deleteZ(field):
    field.delete_subfield('z')


for rec in books:
    if i < limit:
        num_total_books += 1

        for field in rec.get_fields('856'):

            for u in field.get_subfields('u'):

                for domain in weird_domains:
                    if domain in u:
                        rec.remove_field(field)
                        num_fields_removed += 1

                for domain in subscription_domains:
                    if domain in u:
                        print rec.title()
                        prefix(field)
                        num_proxied_ebooks += 1

            if len(field.get_subfields('u')) == 0:
                # 856 is useless without $u, delete the field
                rec.remove_field(field)
                num_fields_removed += 1

            for z in field.get_subfields('z'):
                deleteZ(field)

        processed.write(rec)
        i += 1

processed.close()

# stats
print "\n"
print "Total Records Processed:", num_total_books
print "Ebooks Proxied:", num_proxied_ebooks
print "856s Deleted:", num_fields_removed
print "\n"
