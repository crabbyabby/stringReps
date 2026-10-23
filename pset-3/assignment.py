from pset3 import frequencyArray, transcribeRNA, reverseComplement, findClumps

frequencyArray("ACGCGGCTCTGAAA", 2)
# Expected: [2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0]

transcribeRNA("GATGGAACTTGACTACGTAAATT")
# Expected: "GAUGGAACUUGACUACGUAAAUU"

reverseComplement("AAAACCCGGT")
# Expected: "ACCGGGTTTT"

genome = (
    "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGAC"
    "ATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
)
findClumps(genome, 5, 75, 4)
# Expected: {"CGACA", "GAAGA", "AATGT"} (set order may vary)

print(" ".join(map(str, frequencyArray("ACGCGGCTCTGAAA", 2))))
print(transcribeRNA("GATGGAACTTGACTACGTAAATT"))
print(reverseComplement("AAAACCCGGT"))
print(" ".join(sorted(findClumps(genome, 5, 75, 4))))

