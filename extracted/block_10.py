# Write a FASTA file
# Takes sequence: AA sequence, description : description of sequence, filename: a file name
# Code creates the file, with the required name, write description as a fasta header >, write sequence to the file
# Long sequences should be newline formatted
# Don't return any value, just create the file

# Example: writeFASTA("GALMFWKQESCYHRNDTPVI", "Protein_name", "AA_file.fa")

# Define Function
def writeFASTA(sequence, description, filename):
    
    # Create file in write mode
    file =  open(filename, "w")
    
    # Write header as description, newline 
    file.write(">" + description + "\n")
    
    # Make uppercase
    sequence = sequence.upper()
    
    # Check sequence is AA 
    for i in sequence:
        if i not in "GALMFWKQESCYHRNDTPVI":
            raise BadSequenceException("Input string must be amino acid one character codes only, no special characters")
    
    # Line formatting for sequence
    length = len(sequence)
    for i in range(0, length, 40):
        
        # Write chunks of sequence to file, followed by newline
        file.write(sequence[i:i+40]+ "\n")
        
    # Close file when done
    file.close()
