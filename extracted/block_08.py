#ORF Finder
#Input: string AA sequence
#Output: String of AA's from first Meth (start) to first stop, EXCLUSIVE
#If no Meth or stop, return an empty string

# Example: openReadingFrame("AMCAPP*L") (Stop codons are represented by *)

#define function
def openReadingFrame(aminoacids):
    
    #define start and stop codon symbols
    start = "M"
    stop = "*"
    
    #If a start codon is present, assign it's index to a variable
    if aminoacids.find(start, 0) or aminoacids.startswith(start, 0):
        startindex = aminoacids.find(start, 0)
    
    #If no start codon, return empty string
        if startindex == -1:
            return ""
    
    #If a stop codon is present, assign its index to a variable
    if aminoacids.find(stop, 0):
        stopindex = aminoacids.find(stop, 0)
        
    
    #if no stop codon, return empty string
        if stopindex == -1:
            return ""
    
    #return string of aminoacids from start (Inclusive) to stop (exculsive)
    return aminoacids[startindex:stopindex]

#openReadingFrame("AMCAPP*L")
