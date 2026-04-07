from mergesort import pmerge

def main():
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
            text_file_selection = input("Enter number for text file: ")
            print('')
            filename = list(os.listdir("texts"))[int(text_file_selection) - 1]
            file = open(f"texts/{filename}", "r")
            book = file.read()
            pre_words = book.split(" ")
            word_array = []
            for word in pre_words:
                cleaned = word.strip('"!?.()')
                word_array.append(cleaned)
        
            sorted = pmerge(word_array)

            print("select from menu:" )
            print("1. print sorted list")
            print("2. save sorted list to file")
            print("3. report of occurrences of each word")
            print("4. save report of occurrences of each word to file")
            print("5. return to main menu")
            choice = input("Enter choice: ")
            print('')
            if choice == "1":
                print(sorted)
            if choice == "2":
                with open(f"sorted_{filename}", "w") as f:
                    for word in sorted:
                        f.write(word + "\n")
            if choice == "3":
                from collections import Counter
                word_counts = Counter(sorted)
                for word, count in word_counts.items():
                    print(f"{word}: {count}")

            if choice == "4":
                from collections import Counter
                word_counts = Counter(sorted)
                with open(f"report_{filename}", "w") as f:
                    for word, count in word_counts.items():
                        f.write(f"{word}: {count}\n")

            elif choice == "5":
                continue

        elif choice == "2":
            pass

        elif choice == "3":
            break

if __name__ == "__main__":
    main()