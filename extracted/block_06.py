# SequencePCRtemp
#Take a string fasta file as arg
#Return average melting temp of the two primers as a float

# Example sequencePCRtemp("dna.fa")

# BUG: Doesn't work if the sequence in the file is too short, but produces: 
# AttributeError: 'BadSequenceException' object has no attribute 'upper'
# Although this error relates to using a character orther than "ACGTU", which makes me wonder about \n, " ", etc
# Sequence in FASTA file has to be > 20 nucleotides, so issue with primer function above

#Define sequencePCRtemp
def sequencePCRtemp(file):
    
    #Read input file
    sequence = readDNAsequence(file)
    
    #Get forward and reverse primers
    forward = primer(sequence, forward = True)
    reverse = primer(sequence, forward = False)
    
    #Calculate melttemp for both primers
    f_tm, r_tm = meltingTemp(forward), meltingTemp(reverse)
    print(f_tm, r_tm)
    
    #Average, float() not really required, as python should produce a float from all division
    avg_tm = float((f_tm + r_tm)/2)
    
    return avg_tm

#sequencePCRtemp("dna.fa")
