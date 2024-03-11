"""Find the reverse complement of gene, and identify whether it is the coding strand or template 
strand by searching for the TATAAAA promoter sequence."""

gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"

def complement(seq):
    comp_seq= ""
    for char in seq:
        if char == 'T':
            comp_seq += 'A'
        elif char == 'C':
            comp_seq += 'G'
        elif char == 'A':
            comp_seq += 'T'
        elif char == 'G':
            comp_seq += 'C'
    return comp_seq

complementary_strand = complement(gene)
#print(complementary_strand)

def reverse_complentarystrand(seq):
    return seq[: : -1]

reverse_strand= reverse_complentarystrand(complementary_strand)
print(reverse_strand)
