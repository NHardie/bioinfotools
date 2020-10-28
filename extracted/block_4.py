#Primer(DNA SEQUENCE, LENGTH (20), FORWARD(TRUE))
#When forward = true: return forward primer for sequence, aka forward strand, as it binds to the 3' of the antisense strand
#When forward = false, return reverse primer, aka reverse complement
#length = length of the primer, default 20
#Iff sequence < length, return BadSequenceError

#Using template for complement above to define reverse_complement

# Example: reverse_complement("ACGTTTCG")

# Return of reverse_complement doesn't print any value, might have to split cell to get it to return value to std out?

# Define function
def reverse_complement(dna):
    
    #Make uppercase
    dna = dna.upper()
    
    #Check sequence is actually DNA
    for i in dna:
        if i not in "ACTG":
            raise BadSequenceException("Sequence can't contain characters other than nucleotides", i)
    
    #Create complement dictionary
    dna_complement = {"A": "T", "C": "G", "G":"C", "T": "A"}
    
    #Use list comprehension to loop through 
    dna_comp = [dna_complement[i] for i in dna] 
    
    #Join list together for a string
    #[::-1] for reverse complement
    reverse = "".join(dna_comp)[::-1]
    
    #print(reverse)
    
    # Return reverse complement
    return reverse

#reverse_complement("ACGTTTCG")



#Example : primer("ACTGTGCACGTGCTAGCTGACTGATCG", 10, False)
#Specify parameters to use default for length, but False for forward
#primer("ACTGTGCACGTGCTAGCTGACTGATCG", forward = False)


#Define primer, with default values for length and forward
def primer(sequence, length = 20, forward = True):
    
    #Check primer length isn't longer than that of the sequence
    if length > len(sequence):
        return BadSequenceException("Sequence too short")
    
    #Produce required length of the sequence for the forward primer
    if forward == True:
        return sequence[:length]
    
    #Produce reverse complement of the sequence for the reverse strand
    if forward == False:
        return reverse_complement(sequence)[:length]
    
#primer("ACTGTGCACGTGCTAGCTGACTGATCG", 10, False)
