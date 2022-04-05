from turtle import bgcolor


def colored(dna):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpdna = ""

    for nuc in dna:
        if nuc in bcolors:
            tmpdna += bcolors[nuc] + nuc
        else:
            tmpdna += bcolors['reset'] + nuc
        
    return tmpdna + '\033[0;0m'