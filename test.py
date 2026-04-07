
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

def word_count(word_array):
    count = 0
    for word in word_array:
        count += 1
    return count

def comparision():
    pass