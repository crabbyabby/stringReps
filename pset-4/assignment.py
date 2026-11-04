from pset4 import (
    hammingDistance,
    approximatePatternMatching,
    frequentWordsWithMismatches,
    frequentWordsWithMismatchesAndReverseComplements,
)

p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"
print(hammingDistance(p, q))

pattern = "ATTCTGGA"
string = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
d = 3
print(approximatePatternMatching(pattern, string, d))