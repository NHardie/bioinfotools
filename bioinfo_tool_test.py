from bioinfotools.randDNAStr import *
from bioinfotools.DNA_Validate import *

print(f"Random DNA Sequence: \n{validateseq(dna_seq)}")

from bioinfotools.Nucleotide_counter import *
print(f"Nucleotide frequencies: \n{countnucfrequency(dna_seq)}")

from bioinfotools.DNA_Compliment import *
print(f"Complimentary sequence: \n{dna_compliment(dna_seq)}\nReverse Compliment: \n{reverse_compliment(dna_seq)}")

from bioinfotools.DNA_to_MRNA import *
print(f"mRNA Sequence: \n{mrna(dna_seq)}\n")

print(f"DNA String + Compliment + Reverse Compliment:\nDNA String         5' {dna_seq} 3'")
print(f"                      {''.join(['|' for c in range(len(dna_seq))])}")
print(f"Compiment          3' {dna_compliment(dna_seq)} 5'")
print(f"Reverse Compliment 5' {reverse_compliment(dna_seq)} 3'\n")

from bioinfotools.gc_content import *
print(f"% GC content", gc_content(dna_seq))
