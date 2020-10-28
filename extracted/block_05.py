#Melting temp

#Take primer as a string
#Figure out GC AT counts
#Calculate melting temp of primer in celsius, using equation Tm= 4(G + C) + 2(A + T)
#Raise BadSeqException if characters other than ACTG

#Example: meltingTemp("acgtagctgatcgta")
#Results: Melt temp is: 44 C
         #44


# Define meltingtemp of a primer sequence
def meltingTemp(primer):
    
    # Ensure uppercase
    primer = primer.upper()
    
    # Check all characters represent nucleotides
    for i in primer:
        if i not in "ACTG":
            raise BadSequenceException("Sequence can't contain characters other than nucleotides", i)
    
    # Set a dictionary to store counts
    nucleotide_counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    
    # Fill dictionary with numbers of nucleotides in sequence
    for i in primer:
        nucleotide_counts[i] += 1
    
    # Calculate temprature melt
    tm = 4*(nucleotide_counts["G"] + nucleotide_counts["C"]) + 2*(nucleotide_counts["A"] + nucleotide_counts["T"])
    
    # Nice string formatting
    #print("Melt temp is:",tm, "C")
    
    # Return int value
    return tm

#meltingTemp("acgtgacgtagctgatcg")
