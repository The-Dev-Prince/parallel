import time
from mergesort import pmerge
from MergeSortRegular import merge_sort

# Array builder/splitter
def array_builder(file):
    # Asks for which .txt file to grab from texts folder
    book = file.read()
    # Splits the strings in the .txt file at spaces
    pre_words = book.split(" ")
    # Removes punctuation from the front and end of strings, cleaning up the words
    word_array = []
    for word in pre_words:
        cleaned = word.strip('"!?.()')
        word_array.append(cleaned)

    return word_array

# Calls array_builder function to create test array
# test_array = array_builder()

# Function to count the amount of words that are within a text file
def word_count(text):
    count = 0
    for word in text:
        count += 1
    return count

# Function to compare the times between the regular merge sort and the parallel merge sort
def comparison(text):
    print("Running Merge Sort Algorithms...")
    #Run Regular Merge
    startTime = time.time()
    merge_sort(text)
    endTime = time.time()
    RegularMergeTime = endTime - startTime

    #Run Parallel Merge
    startTime = time.time()
    pmerge(text)
    endTime = time.time()
    ParallelMergeTime = endTime - startTime

    print(f"Regular Merge Sort Time: {RegularMergeTime}\n Parallel Merge Sort Time: {ParallelMergeTime}")

# comparison(test_array)


