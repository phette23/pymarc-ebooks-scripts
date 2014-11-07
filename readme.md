# pymarc scripts

I was shamed into publishing these at LITA Forum 2014. It's not great code, and will need edits in many places (e.g. to point at the right files), but hopefully someone finds it useful.

# notes

This repo is a collection of Python scripts using [pymarc](https://github.com/edsu/pymarc) to clean up our ebook records in our Polaris ILS, specifically it was used to bulk edit MARC records to remove spurious links in them & replace unproxied ebook links with proxied ones. The relevant MARC field is 856$u. Catalogers may find these scripts useful for their work.

The scripts are not very portable so please read them before using, e.g. "proxy-ebooks.py" has a couple highly localized lists of vendor and other URLs in it that only made sense in my specific situation. Almost all the scripts rely on hard-coded filenames in the `MARCReader` and `MARCWriter` lines, which would need to be changed. I haven't included sample MARC files but [the Internet Archive has lots](https://archive.org/details/ol_data) if you want to play.

# table of contents

**count-tag.py** find out many records have a particular tag

**dual856.py** find all your records with multiple [856](http://www.loc.gov/marc/bibliographic/bd856.html) (electronic location) tags

**ebooks-to-csv.py** save all your ebook (defined as anything with an 856 $u) titles to a CSV file

**gmd-counter.py** count number of occurrences of different General Material Designations (245 $h) in a collection of records. Example JSON output included.

**pymarc-notes.md** some very minimal notes on using pymarc, mostly links to documentation

**python-on-windows.md** notes on getting set up on a Windows machine

**proxy-ebooks.py** the main script I wrote, others were basically tests leading up to this. We were implementing a proxy server and this cleaned up our 856 fields while proxying appropriate vendor URLs.

**search-gmd.py** find titles of records with a certain GMD

**subfield-counter.py** count subfields used in all records? I actually don't know, this is horrible code, Eric.

**web-links.py** output stats on 856 fields in records

**webfeet.py** find records with "[selected by Web Feet]" in the title since at some point we imported one of these misguided attempts to catalog "the good parts" of the Internet

**write856s.py** write records with multiple 856 fields out to a separate MARC file

# license

[BSD](http://www.opensource.org/licenses/bsd-license.php) (because pymarc, why not)
