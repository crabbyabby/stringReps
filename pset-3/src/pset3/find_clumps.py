"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""


def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.
    """
    # TODO: Implement clump finding.

    clumps = set()
    frequency_map = {}
    
    first_window = genome[0:L]
    for i in range(L - k + 1):
        kmer = first_window[i:i+k]
        frequency_map[kmer] = frequency_map.get(kmer, 0) + 1
        if frequency_map[kmer] >= t:
            clumps.add(kmer)
            
    for i in range(1, len(genome) - L + 1):
        #remove the kmer in end
        out_kmer = genome[i-1 : i-1+k]
        frequency_map[out_kmer] -= 1
        
        new_kmer_start = i + L - k
        in_kmer = genome[new_kmer_start : new_kmer_start+k]
        frequency_map[in_kmer] = frequency_map.get(in_kmer, 0) + 1
        
        if frequency_map[in_kmer] >= t:
            clumps.add(in_kmer)
            
    return list(clumps)   

    raise NotImplementedError("Implement findClumps for Rosalind BA1E.")


print(findClumps("CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC", 5, 75, 4))