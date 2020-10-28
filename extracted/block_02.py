# Read data from fasta file format
# discard header
# replace U with T
# return sequence as a string

# Example: readDNAsequence("dna.fa")

def readDNAsequence(file):
    
    #Open file with read permissions
    with open(file, "r") as fasta:
        
        #Remove whitespace, return lines as lists. Useful as can easily get headers/ sequences. 
        #Could use .read() to produce a string first, but would still need to strip /n. 
        fas_list = [line.strip() for line in fasta.readlines()]
        
        #Name header, sequence as list indexes
        header, sequence = fas_list[0], fas_list[1:]
        
        #Cat list of sequences into single string
        sequence = "".join(sequence)
        
        #Check sequence is DNA/RNA
        for i in sequence:
            if i not in "ACGTU":
                raise BadSequenceException("Sequence must be nucleotide character, offending character:", i)
        
        #Replace U with T
        sequence = sequence.replace("U", "T")
        
        #Return sequence
        return sequence
    
#readDNAsequence("dna.fa")
