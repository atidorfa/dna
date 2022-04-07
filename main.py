# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import *

seqlength = 50

dna = validateSeq(generateDNA(seqlength))

print("\n")
# print(f"[0] Sequence of DNA: {dna}")
print(f"[0] Sequence of DNA: {colored(dna)}")
print(f"[1] Sequence Lenght: {len(dna)}")
print(colored(f"[2] Nucleotide Frequency: {collectionFrequency(dna)}"))
print(f"[3] DNA/RNA Transcription: {transcription(dna)}")
print("\n")

print(f"[4] DNA String + Complement+ Reverse Complement:")
print(f"5' {colored(dna)} 3'")
print(f"   {''.join(['|' for c in range(len(dna))])} [DNA]")
print(f"3' {colored(reverse_complement(dna)[::-1])} 5' [Complement]")
print(f"5' {colored(reverse_complement(dna))} 3' [Rev. Complement]")
print("\n")

print(f"[5] + GC Content: {gc_content(dna)}%")
print(f"[6] + GC Content in Subsection k=5: {gc_content_subdna(dna, k=5)}")
print("\n")

print(f"[7] + Aminoacids Sequence from DNA: {translate_dna(dna, 0)}")
print(f"[8] + Codon Frequency (L): {codon_usage(dna, 'L')}")
print("\n")