#code for random, small bioinformatics tools
from bioinfotools.randDNAStr import *
#Check input sequence is a Nucleotide string
def validateseq(dna_seq):
    """Checks sequence is DNA by comparing seq with a list of allowed DNA nucleotides"""
    tmpseq = dna_seq.upper()
    for n in tmpseq:
        if n not in Nucleotides:
            return False
    return tmpseq
