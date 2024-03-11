"""write a function complement(), that can take a sequence of DNA and return its complement."""

gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"
seq = "TCAGACTGGTGCCG"

def complement(seq):
    comp_seq=""
    for char in seq:
        if char == 'A':
            comp_seq += 'T'
        elif char == 'T':
            comp_seq += 'A'
        elif char == 'G':
            comp_seq += 'C'
        elif char == 'C':
            comp_seq += 'G'
    return comp_seq


compseq = complement(seq)
print(compseq)