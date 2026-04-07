from mergesort import pmerge
while True:
    print("Select from menu:")
    print("1. sort a file")
    print("2. compare sort times")
    print("3. exit")
    choice = input("Enter choice: ")
    print('')
    if choice == "1":
        print("what file do you want to sort?")
        print("Files in texts folder:")
        import os
        i = 1
        for filename in os.listdir("texts"):
            print(f"{i}. {filename}")
            i += 1
        text_file_selection = input("Enter number of text file: ")
        filename = list(os.listdir("texts"))[int(text_file_selection) - 1]
        file = open(f"texts/{filename}", "r")
        book = file.read()
        pre_words = book.split(" ")
        word_array = []
        for word in pre_words:
            cleaned = word.strip('"!?.()')
            word_array.append(cleaned)
        sorted_words = pmerge(word_array)
        print(sorted_words)

    elif choice == "2":
        pass

    elif choice == "3":
        break
