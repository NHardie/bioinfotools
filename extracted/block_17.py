# Readtable(filename)

# Takes a specified TSV format file 
# Function should return a dict with the file names as keys
# Values should be a list of floats containing the Polar Small and Hydrophobic AA %'s

# Example: readTable("inputfile")

# Define function(Arguments)
def readTable(filename):
    
    # Define dictionary for filename keys and list of floats
    aa_dict = {}
    
    # Open file with context manager
    with open(filename, "r") as infile:
        
        # loop through lines in file
        for line in infile:
            
            # Seperate column titles
            if line.startswith("#"):
                pass
            
            # Split lines, to seperate keys from values
            else: 
                lines = line.split()
                
                # Keys are the first string in the file
                keys = lines[0]
                
                # Values are the following strings, could do [1:], but if any extra values after the 
                # amino acid %'s, might not be good to receive them too for downstream
                values = lines[1:4]
                
                # Turn values into floats, could specify dp with something like %.2f
                values = [float(i) for i in values]
                
                # Populate dictionary with keys and values
                aa_dict[keys] = values
                
    return(aa_dict)
