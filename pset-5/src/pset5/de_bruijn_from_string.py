from pathlib import Path

def deBruijnFromString(k: int, text: str) -> list[list[str]]:
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # TODO: Write your code here.

    # string like AAGATTCTCTAC len(str) = 12
    # AAG -> AGA \\ AGA --> GAT so in sections of k-1

    mappings = []
    for i in range(len(text) - k + 1):
        mappings.append([text[i:i+k-1], text[i+1:i+k]]) 

    mappings = sorted(mappings, key=lambda row: row[0])
    return mappings
    
    raise NotImplementedError("Implement deBruijnFromString")


print(deBruijnFromString(4,"AAGATTCTCTAC"))