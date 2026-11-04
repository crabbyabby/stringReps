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

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
     counts = defaultdict()

     for i in range(len(text)-k):
         kmer = text[i:i+k]
         neighbors = neighbors(kmer, d)

         for pattern in neighbors:
             if hammingDistance(pattern, kmer) < d:
                counts[pattern] += 1

     max_count = max(counts.values())
     returned = []

     for kmer, count in counts:
         if count == max_count:
             returned.append(kmer)
     return returned
        
     raise NotImplementedError("Implement frequentWordsWithMismatches")
