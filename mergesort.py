# the main function

from multiprocessing import Pool

# Array builder/splitter
# Asks for which .txt file to grab from texts folder
text_file = input("Enter name of text file: ")
file = open(f"texts/" + text_file, "r")
book = file.read()
# Splits the strings in the .txt file at spaces
pre_words = book.split(" ")
# Removes punctuation from the front and end of strings, cleaning up the words
word_array = []
for word in pre_words:
    cleaned = word.strip('"!?.()')
    word_array.append(cleaned)

print(word_array)



def merge_sort(lst):
    return lst

def merge(left, right):
    return left, right

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

    result = sorted_chunks[0]
    for chunk in sorted_chunks[1:]:
        result = merge(result, chunk)

    return result


if __name__ == "__main__":
    test = [8, 3, 1, 7, 0, 10, 2, 4]
    print(f"Original: {test}")
    sorted_test = pmerge(test)
    print(f"Sorted:   {sorted_test}")