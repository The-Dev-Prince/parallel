from collections import Counter
from mergesort import pmerge
from test import comparison, array_builder, word_count

def main():
    # Sets word_array variable initially to none so that there are no errors with user selection
    word_array = None

    while True:
        # Main menu
        print("Select from menu:")
        print("1. sort a file")
        print("2. compare sort times")
        print("3. exit")
        choice = input("Enter choice: ")
        print('')
        # Main Menu choice 1: Sort file
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
            word_array = array_builder(file)
        
            sorted = pmerge(word_array)
            print('')

            # Submenu for sorted list
            print("select from menu:" )
            print("1. print sorted list")
            print("2. save sorted list to file")
            print("3. report of occurrences of each word")
            print("4. save report of occurrences of each word to file")
            print("5. return to main menu")
            choice = input("Enter choice: ")
            print('')
            # Submenu choice 1: prints list to terminal
            if choice == "1":
                print(sorted)
                print('')
            # Submenu choice 2: saves sorted list to a new file
            if choice == "2":
                with open(f"sorted_{filename}", "w") as f:
                    for word in sorted:
                        f.write(word + "\n")
                print('')
            # Submenu choice 3: prints the word counts for each word in terminal
            if choice == "3":
                word_count(sorted)
                print('')
            # Submenu choice 4: saves word counts of each word to a new file
            if choice == "4":
                word_counts = Counter(sorted)
                with open(f"report_{filename}", "w") as f:
                    for word, count in word_counts.items():
                        f.write(f"{word}: {count}\n")
                print('')
            #Submenu choice 5: returns user to main menu
            elif choice == "5":
                continue
        
        # Main Menu choice 2: Sort Time comparisons
        elif choice == "2":
            # If user chooses this option before the sort action, this forces user to choose which file to use
            if word_array == None:
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
                word_array = array_builder(file)
                comparison(word_array)
                print('')
            else:
                comparison(word_array)
                print('')
        # Main Menu choice 3: Quits the program
        elif choice == "3":
            break

if __name__ == "__main__":
    main()