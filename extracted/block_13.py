# AAtypes
# Args : string of AA
# Compute the number of aminoacids that are POLAR, SMALL, HYDROPHOBIC in that order

# Example: AAtypes("GALMFWKQESCYHRNDTPVI")
# Other characters than above will produce a Bad Sequence Exception
# (Case-insensitive)

# Define function(arg)
def AAtypes(aaseq):
    
    # Ensure Upper, this is more for downstream analysis
    aaseq = aaseq.upper()
    
    # Ensure characters are aminoacids
    for i in aaseq:
        if i not in "GALMFWKQESCYHRNDTPVI":
            raise BadSequenceException("Input string must be amino acid one character codes only, no special characters")
    
    # Define which AA's are polar, small, hydrophobic
    polar = "YWHKREDTSCNQ"
    small = "VCGSTAP"
    hydrophobic = "FYWHKMCTAILV"
    
    # Counts for the properties
    polar_aa = 0
    small_aa = 0
    hydrophobic_aa = 0
    
    # Iterate through, adding to the counts
    for i in aaseq:
        if i in polar:
            polar_aa += 1
        if i in small:
            small_aa += 1
        if i in hydrophobic:
            hydrophobic_aa += 1
    
    # String the counts
    aa_string = (polar_aa, small_aa, hydrophobic_aa)
    
    # Get length of sequence
    length = len(aaseq)
    
    # Work out % of sequence
    aa_percent = (polar_aa/length, small_aa/ length, hydrophobic_aa/ length) 
    
    # Output as a list
    aa_list = list(aa_percent)

    # Return output
    return aa_list
    
