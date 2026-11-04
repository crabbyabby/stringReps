def hammingDistance(p: str, q: str) -> int:
    # TODO: Write your code here.
    count = 0
    for c1, c2 in zip(p, q):
        if c1 != c2:
            count += 1
    return count

    raise NotImplementedError("Implement hammingDistance")
