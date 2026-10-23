"""Rosalind BA1K: Generate the Frequency Array of a String."""

def findValue(kmer: str) -> int:
    nucleotides = {"A": 0, "C": 1, "G": 2, "T": 3}
    value = 0 
    
    for char in kmer:
        value = (value * 4) + nucleotides[char]
        
    return value

def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    # TODO: Implement the frequency array.

    freqArray = [0] * (4**k)
    nucleotides = ["A", "C", "G", "T"]

    # base 4, ie k = 4 has 256 options. so base 4 is 1, 4, 16, 64
    # k = 3 has 64 options, 1, 4, 16
    # k =2 has 16 options
    # A=0, B=1, C=2, D=3
    # AAA = 0. 
    # DDD = 63 = 16*3 + 4*3 + 1*3

    # Looks at the kmer, adds 1 to the array index it corresponds to.

    for i in range(len(text)-k):
        kmer = text[i:i+k]
        val = findValue(kmer)
        freqArray[val] += 1

    return freqArray
    raise NotImplementedError("Implement frequencyArray for Rosalind BA1K.")
