def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid. A string is not a
    valid DNA sequence if it contains lowercase letters.

    >>> is_valid_sequence('ATAGCCGTA')
    True
    >>> is_valid_sequence('ATaGccGTB')
    False

    """

    for char in dna:
        if char not in 'ATCG':
            return False
    return True


def insert_sequence(dna1, dna2, index):

    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>> insert_sequence('ATTA', 'CG', 1)
    ACGTTA
    >>> insert_sequence('CGTTAC', 'TCG', 3)
    CGTTCGTAC
    
    """

    result = dna1[:index] + dna2 + dna1[index:]
    return result


def get_complement(dna):

    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    >>> get_complement('T')
    A

    """

    if dna == 'A':
        return 'T'
    if dna == 'T':
        return 'A'
    if dna == 'C':
        return 'G'
    if dna == 'G':
        return 'C'
    return 'Invalid nucleotide'

def get_complementary_sequence(sequence):

    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('ATTA')
    TAAT
    >>> get_complementary_sequence('CTAG')
    GATC
    >>> get_complementary_sequence('AGTTACGT')
    TCAATGCA

    """
    
    result = ''
    
    for char in sequence:
        result += get_complement(char)
    return result   
        
