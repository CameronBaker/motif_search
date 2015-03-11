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

	desc = "at 90%25 Sequence"
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
	<identityCutoff>90</identityCutoff>
	</orgPdbQuery>
	</queryRefinement>
	</orgPdbCompositeQuery>
	""" % (motif,motif,desc)

	desc = "at 95%25 Sequence"
	queryText3 = """
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
	<identityCutoff>95</identityCutoff>
	</orgPdbQuery>
	</queryRefinement>
	</orgPdbCompositeQuery>
	""" % (motif,motif,desc)

	desc = "at 100%25 Sequence"
	queryText4 = """
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
	req3 = urllib2.Request(url, data=queryText3)
	req4 = urllib2.Request(url, data=queryText4)

	f = urllib2.urlopen(req)
	f2 = urllib2.urlopen(req2)
	f3 = urllib2.urlopen(req3)
	f4 = urllib2.urlopen(req4)

	r1 = f.read().count('\n')
	r2 = f2.read().count('\n')
	r3 = f3.read().count('\n')
	r4 = f4.read().count('\n')
		
	if (r1 and r2 and r3 and r4):
	    print motif,",",r1,",",r2,",",r3,",",r4,"\n"
	else:
	    print "Failed to retrieve results" 

print "motif,","hit,","90,","95,","100\n"
with open(sys.argv[1]) as f:
	lines = (line.rstrip('\n') for line in f)
	for l in lines:
		motifSearch(l)
