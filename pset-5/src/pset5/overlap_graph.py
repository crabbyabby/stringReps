from pathlib import Path
def overlapGraph(patterns: list[str]) -> list[list[str]]:
    """Return the overlap graph as rows [source, destination] (BA3C).

    Each row contains one directed edge, with the source first.
    Row order does not matter.
    """
    # TODO: Write your code here.

    # if last 4 match up with first 4 of another list.

    graph = {}

    length = len(patterns[0])

    for i, kmer in enumerate(patterns): # for each kmer suffix
        for j, kmer2 in enumerate(patterns): # check against every single kmer prefix
            if i!=j:
                if kmer2.startswith(kmer[1:length]):
                    graph.setdefault(kmer, []).append(kmer2)
 
    graph = dict(sorted(graph.items(), key=lambda item: item[0]))
    return graph


    raise NotImplementedError("Implement overlapGraph")

lst = []
file_path = Path(__file__).resolve().parent / "rosaline_ba3c.txt"
with open("rosalind_ba3c.txt", "r", encoding="utf-8") as file:
    for line in file:
        lst.append(line.strip())

graph = overlapGraph(lst)
with open("output.txt", "w", encoding="utf-8") as file:
    for node, edge in graph.items():
        file.write(f"{node} -> {edge[0]}\n")
