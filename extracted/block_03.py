#Complement dna sequence
#Take dna sequence
#Check for bad sequence error
#Swap complements
#return string

#Example: complement("ACGTTTCG")

# Define function
def complement(dna):
    
    #Make uppercase
    dna = dna.upper()
    
    #Check sequence is actually DNA
    for i in dna:
        if i not in "ACTG":
            raise BadSequenceException("Sequence can't contain characters other than nucleotides", i)
    
    #Create complement dictionary
    dna_complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    
    #Use list comprehension to loop through 
    dna_comp = [dna_complement[i] for i in dna] 
    
    #Join list together for a string
    #Can add [::-1] for reverse complement
    return "".join(dna_comp)

#complement("ACGTTTCG")
