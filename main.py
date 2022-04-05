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
print(f"[4] DNA Reverse Complement: {reverse_complement(dna)}")
print("\n")

print(f"DNA + DNA REVERSE COMPLEMENT:\n")
print(f"5' {colored(dna)} 3'")
print(f"   {''.join(['|' for c in range(len(dna))])}")
print(f"3' {colored(reverse_complement(dna))} 5'")
print("\n")