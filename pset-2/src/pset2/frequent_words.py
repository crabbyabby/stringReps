from .pattern_count import patternCount

t = "CACTAAGCGCCACCGGCACTAAGCGTAAAAACACGTCAGGTGTCACTAAGCGCCACCGGCACTAAGCGTAAAAACACGTCAGGTGTCCACCGGCCACCGGCACTAAGCGGTCAGGTGTTAAAAACACCCACCGGGTCTCCTCCACTAAGCGTAAAAACACCCACCGGCCACCGGCCACCGGGTCAGGTGTCCACCGGCCACCGGTAAAAACACGTCTCCTCTAAAAACACGTCTCCTCGTCAGGTGTGTCTCCTCCACTAAGCGGTCAGGTGTTAAAAACACGTCTCCTCCCACCGGCCACCGGCACTAAGCGTAAAAACACCCACCGGCCACCGGCCACCGGGTCTCCTCGTCTCCTCCCACCGGGTCTCCTCCACTAAGCGCCACCGGTAAAAACACGTCAGGTGTGTCAGGTGTTAAAAACACCCACCGGTAAAAACACGTCTCCTCCACTAAGCGCACTAAGCGGTCAGGTGTCACTAAGCGGTCTCCTCGTCAGGTGTCCACCGGGTCTCCTCCCACCGGGTCAGGTGTTAAAAACACCCACCGGCCACCGGCACTAAGCGGTCTCCTCCACTAAGCGCCACCGGCCACCGGTAAAAACACGTCAGGTGTGTCAGGTGTTAAAAACACGTCTCCTCCCACCGGCACTAAGCGGTCAGGTGTTAAAAACACGTCAGGTGTCCACCGGCCACCGGTAAAAACACCCACCGGTAAAAACACGTCTCCTCTAAAAACACCCACCGGTAAAAACACTAAAAACACCACTAAGCGGTCTCCTCGTCTCCTCTAAAAACACCACTAAGCGCCACCGGCACTAAGCGTAAAAACAC"
l = 13

def frequentWords(text: str, k: int) -> set[str]:

    frequentPatterns = set()
    counts= []
    i = 0
    while i < len(text)-k:
        pattern = text[i:i+k]
        counts.append(patternCount(text, pattern))
        i = i+1
    
    maxCount = max(counts)

    i = 0
    while i < len(text)-k:
        if(counts[i]== maxCount):
            frequentPatterns.add(text[i:i+k])
        i = i+1

    answer = ""
    for item in frequentPatterns:
        answer += str(item) + " "
    return answer.strip()



print(frequentWords(t, l))


# Potentially more efficient implementation start

# def fWords(text, k):
#     patterns = {}
#     for i in range (len(text)-k):
#         pattern = text[i:i+k]
#         if pattern in patterns:
#             patterns[pattern] += 1
#         else:
#             patterns[pattern] = 1

#     maxCount = max(patterns.values())
    