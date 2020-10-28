#Translate
#Takes a string of DNA
#Outputs dictionary of translated DNA sequence in all 6 reading frames
#Keys should be f1, f2, f3, r1, r2, r3
#Don't complement the sequence, just reverse 
#Highlight stop codons with an *

#Need Amino Acid dictionary to translate nucleotide codons
#M is start, * is a stop

aa_dict = { 
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W', 
    } 


def translate(sequence):
    
    #First translate sequence 
    #sequence = sequence.replace("T", "U")
    
    # Make Upper case
    sequence = sequence.upper()
    
    #Check sequence is DNA
    # (Would swap T for U in the string below)
    for i in sequence:
        if i not in "ACGT":
            raise BadSequenceException("Input string must be DNA Nucleotides only, no special characters")
        
    #Get length of sequence
    length = len(sequence)
        
    #Define start position for reading frames
    start_position = 0
        
    #Define reading frames, need to reduce the full length to avoid key errors
    forward_1 = range(start_position, length - 2, 3)
    forward_2 = range(start_position + 1, length - 2, 3)
    forward_3 = range(start_position + 2, length - 2, 3)
        
    #Create empty dictionary for resulting proteins
    reading_frame_dict = {}
        
    #reverse the sequence for reverse reading frames
    rev_seq = sequence[::-1]
        
    #generate codon lists to transform into proteins
    codons_f1 = [sequence[i:i+3] for i in forward_1]
    codons_f2 = [sequence[i:i+3] for i in forward_2]
    codons_f3 = [sequence[i:i+3] for i in forward_3]
        
    codons_r1 = [rev_seq[i:i+3] for i in forward_1]
    codons_r2 = [rev_seq[i:i+3] for i in forward_2]
    codons_r3 = [rev_seq[i:i+3] for i in forward_3]
        
        
    #Add proteins to dictionary
    reading_frame_dict["f1"] = "".join([aa_dict[i] for i in codons_f1])
    reading_frame_dict["f2"] = "".join([aa_dict[i] for i in codons_f2])
    reading_frame_dict["f3"] = "".join([aa_dict[i] for i in codons_f3])
    reading_frame_dict["r1"] = "".join([aa_dict[i] for i in codons_r1])
    reading_frame_dict["r2"] = "".join([aa_dict[i] for i in codons_r2])
    reading_frame_dict["r3"] = "".join([aa_dict[i] for i in codons_r3])
    
        
    return(reading_frame_dict)

#translate("ACTGACTGACTGACTGACTGACTG")
