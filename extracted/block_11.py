# Maximal ORF
# Input: argument string inputfile, name of a file
# Output: argument string outputfile, name of the file
# Takes proteinname as argument, description of protein 
# Function reads dna sequence from the input file, finds the longest ORF and writes to the output, as fasta
# proteinname should provide the header to the FASTA file
# Shouldn't return any value

# Example: maximalORF("dna.fa", "long_orf", "Fasta header")

# Define function
def maximalORF(inputfile, outputfile, proteinname):
    
    # Open file with context manager
    with open(inputfile, "r") as infile:
    
        # Send header and sequence to empty lists
        header = []
        sequence = []
        
        # Seperate header and sequence
        for line in infile:
            if line.startswith(">"):
                header = line
            else:
                sequence += line
                
        # Join list to form string
        sequence = "".join(sequence)
        
        # Tidy newlines
        sequence = sequence.replace("\n", "")
        
        #Find longest ORF
        longorf = candidateProtein(sequence)
   
    # Write to new file
    writeFASTA(longorf, proteinname, outputfile)

