# distanceMatrix(inputfile, outputfile)
# Function reads input file, creates matrix of size NxN where N = number of proteins in inputfile
# (+ 1 row and column for labels)
# Rows and columns should equal protein file names, so each matrix entry = a pair of proteins
# The entry should correspond to the distance between the lists, considered as 3 dimensional vectors
# Could be symmetrical and have 0's on the diagonals
# no return value

#Might be easier to use pandas or something similar, but not sure what is avaliable from the std library

# Example: distanceMatrix("inputfile", "outputfile")

# Define function
def distanceMatrix(inputfile, outputfile):
    
    # Create file in write mode
    newfile =  open(outputfile, "w")
    
    # Open file with context manager
    with open(inputfile, "r") as infile:
       
        keylist = []
        valuelist = []
        
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
                keylist += [keys]
                
                # Values are the following strings, could do [1:], but if any extra values after the 
                # amino acid %'s, might not be good to receive them too for downstream
                values = lines[1:4]
                
                # Turn values into floats, could specify dp with something like %.2f
                values = [float(i) for i in values]
                valuelist += [values]
    
    #File names
    keystring = "\t".join(keylist)
    
    #Produce column headers
    column_heads = ("#" + "Filename" + "\t" + "{}").format(keystring)
    
    #write column heads
    newfile.write(column_heads)
    
    #Get number of files to use
    count = len(keylist)
       
    #Rows should be in this format, newline from column heads, file, tab, variable number of results to populate "matrix"
    rows = ("\n" + "{}" + "\t" + "{}" + "\t")

    # Store results outside of for loop
    row_pop = []
    
    # loop through a loop to calculate all combinations of values, aa, ab, ac..., ba, bb, bc ...
    for i in range(0, count, 1):
        for n in range(0, count, 1):
            
            # Calculates distances for each combination of values
            # This works as intended, but float objects
            row_pop += [distance(valuelist[i], valuelist[n])]    
    
    # Could just use count, but clearer to read this way
    n = count
    
    # Can split row pop into chunks, could float then input into rows
    # If I tab seperate here, I can't call row_chunks[index] later
    row_chunks = [row_pop[i:i + n] for i in range(0, count**2, n)]
    
    # If I tab seperate here, I seperate the titles too
    for i in range(0, count):
        row_values = rows.format(keylist[i], row_chunks[i])

        # Split the list
        splitted = row_values.split(" ")
        
        # Rejoin with tabs
        tab_join = ("\t".join(splitted))
        
        # Clean away the [] from the old list
        clean = str(tab_join).replace('[','').replace(']','')
        
        # Write to newfile
        newfile.write(clean)

