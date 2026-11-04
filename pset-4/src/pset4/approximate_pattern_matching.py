def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    # TODO: Write your code here.
    indices = []
    for i in range(len(text)-len(pattern)):
        substring = text[i:i+len(pattern)]

        count = 0
        for c1, c2 in zip(substring, pattern):
            if c1 != c2:
                count += 1
        if count <= d:
            indices.append(i)
        
    return indices

    raise NotImplementedError("Implement approximatePatternMatching")
