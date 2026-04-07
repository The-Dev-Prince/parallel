# the main function

from multiprocessing import Pool
from MergeSortRegular import merge_sort


def pmerge(lst, agents = 4):

    if len(lst) <= 1:
        return lst
    
    chunklen = len(lst) // agents
    chunks = []
    for i in range(agents):
        if i == agents - 1:
            chunks.append(lst[i*chunklen:])
        else:
            chunks.append(lst[i*chunklen:(i + 1)*chunklen])

    with Pool(processes = agents) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    while len(sorted_chunks) > 1:
        sorted_chunks = [merge_sort(sorted_chunks[i] + sorted_chunks[i + 1]) for i in range(0, len(sorted_chunks) - 1, 2)]

    return sorted_chunks[0]

if __name__ == "__main__":
    test = [8, 3, 1, 7, 0, 10, 2, 4]
    print(f"Original: {test}")
    sorted_test = pmerge(test)
    print(f"Sorted:   {sorted_test}")