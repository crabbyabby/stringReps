import itertools
from collections import defaultdict
from pset4 import hammingDistance

def neighbors(pattern: str, d: int):
    if d == 0:
        return {pattern}

    neighbors = set()
    short_neighbors = neighbors(pattern[1:], d)

    for kmer in short_neighbors:
        if hammingDistance(pattern[1:], kmer) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighbors.add(nucleotide + kmer)
        else:
            neighbors.add(pattern[0] + kmer)
    return neighbors

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    # TODO: Write your code here.
    bases = ['A', 'C', 'G', 'T']


    for i in range(len(text) - k):
        if 
        

    raise NotImplementedError("Implement frequentWordsWithMismatchesAndReverseComplements")
