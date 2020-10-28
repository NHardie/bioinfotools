# AAtypetable
# Input: List of strings called filelist, outputfile
# Each string in list filelist = the name of a fasta file with an AA sequence
# For each filename, load the sequence, compute the fractions of AA's which are polar, small, hydrophobic
# Output to outputfile as TSV
# Include a # for the column headers
# 2 D.P.

# Example: AAtypetable(["AA_1.fa", "AA_2.fa"], "output")

# Define function (Args)
def AAtypetable(filelist, outputfile):   
    
    # Create file in write mode
    file =  open(outputfile, "w")
        
    # Write column titles, tab-seperated, newline
    file.write("#" + "Filename" + "\t"+ "Polar" + "\t" + "Small" + "\t" + "Hydrophobic" + "\n")
    
    # Define count and problem files list
    count = 0
    problem_files = []
    
    # Loop through list of filenames
    for i in filelist:
            
            #Try code
            try:
                
                # Assign variables to iterate through list
                filename = filelist[count]
                
                # Assign variables using prior function
                sequence = readAAsequence(i)
                
                polar, small, hydrophobic = AAtypes(sequence)
                
                # Format to output using string formatting
                sequence = ("{}" + "\t" + "{}" + "\t" + "{}" + "\t" + "{}" + "\n").format(filename, polar, small, hydrophobic)
                
                # Write to output file
                file.write(sequence)
                
                # Increase the count to move to next iterable in list
                count += 1
            
            # Except problem files, empty, blank
            except:
                
                # Put problem files in empty list
                problem_files.append(i)
            
    # Close file when done
    file.close()
    
    # Return list of problem files, or empty list if all successful
    return problem_files
