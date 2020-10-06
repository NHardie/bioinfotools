#Calculate GC content of a DNA sequence
def gc_content(seq):
    return round(
        ((seq.count("C") + seq.count("G")) / len(seq) * 100), 6)
