

# Import the sequence from the Biopython library
from Bio.Seq import *

# Define a sequence as a DNA Seq object
seq = Seq("CCTCAGCGAGGACAGCAAGGGACTAGCC")

# The complement() method can act just like your complement() function.
complement = seq.complement()

# Similarly, we can use the reverse_complement() method.
reverse_complement = seq.reverse_complement()

# We can even use the transcribe() method to switch alphabets to RNA 
RNA = seq.transcribe()

print(RNA)