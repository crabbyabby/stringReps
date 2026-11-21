from collections import defaultdict
def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # TODO: Write your code here.

    graph = []
    length = len(patterns[0])
    for kmer in patterns:
        prefix = kmer[0:length-1]
        suffix = kmer[1:length]

        for node in graph: # checking every single already in there prefix if it's equal
            if node[0] == prefix:
                node.append(suffix)
                break
        else:
            graph.append([prefix, suffix])
        
    return graph
    raise NotImplementedError("Implement deBruijnFromKmers")

patterns = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]

print(deBruijnFromKmers(patterns))