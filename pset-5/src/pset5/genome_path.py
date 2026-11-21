from pathlib import Path

def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    # TODO: Write your code here.

    # add the kmer every k kmers, and then some of the last one if there is overflow. find how much nucleotide
    # to add with mod

    k = len(patterns[0])
    last = 0

    genome = ""
    for i in range(0, len(patterns), k):
        genome += patterns[i]
        last = i
    missing = len(patterns) - 1 - last
    if missing > 0:
        genome += patterns[-1][-missing:]

    return genome
    raise NotImplementedError("Implement stringSpelledByGenomePath")

# pattern = []
# file_path = Path(__file__).resolve().parent / "rosaline_ba3c.txt"
# with open("rosalind_ba3c.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         pattern.append(line.strip())

# print(pattern)
# print(stringSpelledByGenomePath(pattern))
