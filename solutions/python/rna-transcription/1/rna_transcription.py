def to_rna(dna_strand):
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