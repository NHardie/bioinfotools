# readAAsequence
# Input argument: filename 
# Takes file with AA sequence, function reads the file, discards the header, returns sequence as a string

# Need to add a way to catch non-fasta files

#Example: readAAsequence("AA.fa")

# Define function(args)
def readAAsequence(inputfile):
    
    # Open file with context manager
    with open(inputfile, "r") as infile:
        
        # Define empty lists for header and sequence values
        header = []
        sequence = []
        
        first_line = infile.readline().strip()
        if first_line.startswith(">"):
            pass
        else:
            raise BadSequenceException("""File doesn't seem to be in FASTA format, the FASTA header should start with a >
            > FASTA HEADER
            SEQUENCEINFORMATION
            """)
        
        # Find header, sequence
        for line in infile:
            if line.startswith(">"):
                header = line
            else:
                sequence += line
        
        # Turn list into single string
        sequence = "".join(sequence)
        
        # Tidy up newlines
        sequence = sequence.replace("\n", "")
        
        # Return AA sequence
        return sequence
