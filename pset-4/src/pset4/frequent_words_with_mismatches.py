from itertools import product

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    # TODO: Write your code here.

    bases = ['A', 'C', 'G', 'T']

    kmers = [''.join(p) for p in product(bases, repeat=k)]

    for i in range(len(text) - k):
        if 
        
    raise NotImplementedError("Implement frequentWordsWithMismatches")
