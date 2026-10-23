"""Rosalind BA1K: Generate the Frequency Array of a String."""


def frequencyArray(rosalind: bool, text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    # TODO: Implement the frequency array.

    freqArray = [0] * (4**k)
    nucleotides = ["A", "C", "G", "T"]

    # base 4, ie k = 4 has 256 options. so base 4 is 1, 4, 16, 64
    # base 3 has 64 options. 1, 3, 9 (?)
    # base 2 has 16 options 1, 2 (?).
    # these values multiply by what letter is at each index. so (base 3) CAD = 
    # AAA = index 0. 9*0 + 3*0 + 1*0 = 0.
    # DDD = index 80. 9*3 +  

    # AAAA = 0, AABA = 
    for i in range(k)


    for first in nucleotides:
        for second in nucleotides:
            pair = first + second
            freqArray[pair] = 0

    for i in range(len(text) - k):
        kmer = text[i:i+k]
        freqArray[kmer] += 1

    if rosalind:
        returned = ""
        for value in freqArray.values():
            returned = str(value) + " "

        return returned.strip()

    else:
        return freqArray
    raise NotImplementedError("Implement frequencyArray for Rosalind BA1K.")


print(frequencyArray(True, "AACCGGTAGCTGGTCCGAGGATGCAACTATAGACTTGGACGAGCCTACTTTAAACGCCTTTGAAGTTCTTTATTCTTACGGTCCTCTACAACTAGCGAGCAGGTGAAGTGCATCATAAACAAAAGTAGATCCTTGACGCGGCAACGGGATGGTCAATACGTACCATAGGAATATACGGGTCGGAAGTTTGCATCCAGATGTCGAACTCCAAAAAAAATGTTACTGTCCCTCTAGCGTGACGAGCTAGAACAAAATGGTTAAGAGGAGAAATTATTACTACACTGGTCCCTGTATCCGCAAGTCAGTCAAGGAGGTAGTGTTGTCGCGGGTAATATTGACCATCGCTAATGCATACTGCGTGCTACAATTGGAACGTTTGGTCCATGGGTGGTCGTAGTTTGCTTAACGACCATAGACGGACATGATAAGGAAAGGGTATCATGTAGCCATGTCGCGAGGACTAACCACGGTCCGGTCAACCCGCTCCGCGTCAACTGTGGCCACTCTGTAGTTTTTCCATGCAACATGCATTGTCAAGATGTGAACAACATGGTCTCCATTACAGTCATTTGGAAACTACATCCGGTAGTTATTAAGACATCTTAATATGCTTTTACACCCGGAGCTCCTATCTGATTACACTAGTACATAAGAGCTCGCCCTTAGTTAGGCAATTATCACTCCAGTTGCTTGAGTACCCACAGGTCATCATTATTTTG", 6))