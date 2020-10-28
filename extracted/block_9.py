#Translating a sequence
#Take DNA string input
#output: String of aminoacids corresponding to the longest ORF

# Example: candidateProtein("ATGACTGACTGACTGTAGACTGACTGACTG")

#Define function
def candidateProtein(sequence):
    
    # Make uppercase
    sequence = sequence.upper()
    
    # Check sequence is DNA
    for i in sequence:
        if i not in "ACGT":
            raise BadSequenceException("Input string must be DNA Nucleotides only, no special characters")
    
    #translate all reading frames
    reading_frames = translate(sequence)
    
    #Use list comprehensions to find ORF
    orf = [openReadingFrame(reading_frames[k]) for k in reading_frames]
    
    #Return the largest of the ORF's
    return(max(orf))
