from stats import spliting_text
from stats import character_count
from stats import sort_characters
import sys 

def get_book_text(path):
    # defining the file_contents to be empty first
    file_contents = ""
    # opening the file in read mode with utf-8 encoding
    with open(path, "r", encoding="utf-8") as f:
        # reading the contents of the file 
        file_contents = f.read()
        # returning the contents of the file
    return file_contents 


def main():

    # Check if the user has provided excactly one argument (script + path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Get the path from the command line  
    book_path = sys.argv[1]

    # Now you can use your existing logic right below

    book_text = get_book_text(book_path)
    count_characters = character_count(book_text)
    count_words = spliting_text(book_path)
    sorted_counts = sort_characters(count_characters)
    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    # Print every character and its count
    for item in sorted_counts:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()



