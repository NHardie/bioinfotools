from bioinfotools.Nucleotide_counter import *

dna_seq = dna_seq

Nucleotides = ["A", "C", "G", "T"]
dna_reverse_compliment = {"A": "T", "C": "G", "G": "C", "T": "A"}

def reverse_compliment(dna_seq):
    return "".join([dna_reverse_compliment[dna] for dna in dna_seq])[::-1]

def dna_compliment(dna_seq):
    return "".join([dna_reverse_compliment[dna] for dna in dna_seq])
