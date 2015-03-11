"""
Cameron Baker
This script searchs for all structures with atleast 95% _sequence identity and prints
the list to an output file to be run in with a batch script
"""

import sys
import urllib2

def motifSearch(motif):
	url = 'http://www.rcsb.org/pdb/rest/search'
	queryText = """
	<orgPdbCompositeQuery version="1.0">
	<queryRefinement>
	<queryRefinementLevel>0</queryRefinementLevel>
	<orgPdbQuery>
	<version>head</version>
	<queryType>org.pdb.query.simple.EnzymeClassificationQuery</queryType>
	<description>Enzyme Classification Search : EC=%s</description>
	<Enzyme_Classification>%s</Enzyme_Classification>
	</orgPdbQuery>
	</queryRefinement>
	</orgPdbCompositeQuery>
	""" % (motif,motif)


	req = urllib2.Request(url, data=queryText)

	f = urllib2.urlopen(req)

	result = f.read()

	if (result):
	    print result
	else:
	    print "Failed to retrieve results" 

motifSearch(sys.argv[1])
