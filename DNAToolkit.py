# DNA Toolkit file
from structures import *
import random
import collections


# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucliotides:
            return False
    return tmpseq


# Generate DNA
def generateDNA(l):
    dna = ''.join([random.choice(Nucliotides)
                for nuc in range(l)])

    return validateSeq(dna)


# Count frequency of nucliotides
def countNucFrequency(dna):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict


def collectionFrequency(dna):
    return dict(collections.Counter(dna))


# DNA -> RNA Transcription
def transcription(dna):
    '''DNA -> RNA Transcription. Replacing Thymine with Uracil'''
    return dna.replace("T", "U")


# DNA Reverse Complement
def reverse_complement(dna):
    '''Swap Adenine with Thymine and Guanine with Cytosine. Reversing newly generated string'''
    return ''.join([dna_reversecomplement[nuc] for nuc in dna])[::-1]

    #  # python approach. faster solution
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return dna.translate(mapping)[::-1]


def gc_content(dna):
    '''GC Cotent in DNA/RNA sequences'''
    return round((dna.count('C') + dna.count('G')) / len(dna) * 100)


def gc_content_subdna(dna, k=20):
    '''GC Cotent in DNA/RNA sub-sequence lenght k. k=20 by default'''
    res = []
    for i in range(0, len(dna) - k + 1, k):
        subdna = dna[i:i + k]
        res.append(gc_content(subdna))
    return res