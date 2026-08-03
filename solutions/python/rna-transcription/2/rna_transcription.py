def to_rna(dna_strand):
    '''
    Function to transpose dna strand information to its rna compliment form.
    '''
    rna_compl = ""
    for nuc in dna_strand:
        if nuc == "G":
            rna_compl = rna_compl + "C"
        elif nuc == "C":
            rna_compl = rna_compl + "G"
        elif nuc == "T":
            rna_compl = rna_compl + "A"
        elif nuc == "A":
            rna_compl = rna_compl + "U"
    return rna_compl