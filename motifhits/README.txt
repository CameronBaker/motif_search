Cameron Baker

This script is designed to take in a file consisting of single lines of motifs,
at one motif per line. It then searchs the pdb for the number of proteins
corresponding to that motif. After that it searches the pdb for the number of proteins
with 90%, 95%, and 100% structure identity. 
This program is designed to be piped to an output file.
It is based off the example hosted on the pdb:

http://www.rcsb.org/pdb/software/static.do?p=/software/webservices/search_nmr.jsp

Usage: python squeryScript motiflist.txt
Output for motif 1.1.1.149: 1.1.1.149, 6, 2, 2, 3

This script will be updated to be more generic in the future