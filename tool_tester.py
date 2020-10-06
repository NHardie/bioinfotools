#Code to generate a random string of nucleotides

import random

Nucleotides = ["A", "C", "G", "T"]

#Create a random string of nucleotides
#With length x where for n in range(x)])

dna_seq = "".join([random.choice(Nucleotides)
                      for n in range (20)])

from bioinfotools.randDNAStr import *
#Check input sequence is a Nucleotide string
def validateseq(dna_seq):
    tmpseq = dna_seq.upper()
    for n in tmpseq:
        if n not in Nucleotides:
            return False
    return tmpseq

#Code to count occurences of nucleotides in a string
#Relies upon Nucleotides list as found in bioinfotools.DNA_Validate.py
from bioinfotools.DNA_Validate import *

def countnucfrequency(dna_seq):
    tempfreqdict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for n in dna_seq:
        tempfreqdict[n] += 1
    return tempfreqdict

dna_seq_valid = (validateseq(dna_seq))
print(dna_seq_valid)
print(countnucfrequency(dna_seq_valid))
