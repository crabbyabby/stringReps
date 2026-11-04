import itertools
from collections import defaultdict
from pset4 import hammingDistance
from pset3 import reverseComplement

def find_neighbors(pattern: str, d: int):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighbors = set()
    short_neighbors = find_neighbors(pattern[1:], d)

    for kmer in short_neighbors:
        if hammingDistance(pattern[1:], kmer) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighbors.add(nucleotide + kmer)
                neighbors.add(reverseComplement(nucleotide + kmer))
        else:
            neighbors.add(pattern[0] + kmer)
    return neighbors

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
     counts = defaultdict(int)

     for i in range(len(text)-k+1):
         kmer = text[i:i+k]
         near = find_neighbors(kmer, d)

         for pattern in near:
             counts[pattern] += 1

     max_count = max(counts.values())
     returned = []

     for kmer, count in counts.items():
         if count == max_count:
             returned.append(kmer)
     return returned
        
     raise NotImplementedError("Implement frequentWordsWithMismatches")
