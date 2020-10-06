#Code to count occurences of nucleotides in a string
#Relies upon Nucleotides list as found in bioinfotools.DNA_Validate.py
#Can remove from bioinfotools, just add variable Nucleotides = ["A", "C", ...]
from bioinfotools.DNA_Validate import *

def countnucfrequency(dna_seq):
    tempfreqdict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for n in dna_seq:
        tempfreqdict[n] += 1
    return tempfreqdict
