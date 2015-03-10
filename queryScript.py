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

	desc = "at 100%25 Sequence"
	queryText2 = """
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
	<queryRefinement>
	<queryRefinementLevel>1</queryRefinementLevel>
	<conjunctionType>and</conjunctionType>
	<orgPdbQuery>
	<version>head</version>
	<queryType>org.pdb.query.simple.HomologueEntityReductionQuery</queryType>
	<description>Representative Structures %s Identity</description>
	<identityCutoff>100</identityCutoff>
	</orgPdbQuery>
	</queryRefinement>
	</orgPdbCompositeQuery>
	""" % (motif,motif,desc)


	req = urllib2.Request(url, data=queryText)
	req2 = urllib2.Request(url, data=queryText2)

	f = urllib2.urlopen(req)
	f2 = urllib2.urlopen(req2)

	result = f.read()
	result2 = f2.read()

	if (result and result2):
	    tmp = float(result2.count('\n')) / result.count('\n')
	    print motif,", ",result2.count('\n'),", ",result.count('\n'),",",tmp 
	else:
	    print "Failed to retrieve results" 

with open(sys.argv[1]) as f:
	lines = (line.rstrip('\n') for line in f)
	print "Run includes the template residue"
	for l in lines:
		motifSearch(l)
