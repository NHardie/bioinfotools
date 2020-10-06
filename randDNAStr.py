#Code to generate a random string of nucleotides

Nucleotides = ["A", "C", "G", "T"]
import random

#Create a random string of nucleotides
#With length x where for n in range(x)])

dna_seq = "".join([random.choice(Nucleotides)
                      for n in range (40)])

#If a known sequence of nucleotides is required, input sequence as dna_seq = "USER SEQUENCE" #-out the randomiser
#like so:
#dna_seq = "ATCGTGATGCCGGTACAATGTTT"
            #"".join([random.choice(Nucleotides)
                        #for n in range (x)])
#Where x is the length of random sequence required
