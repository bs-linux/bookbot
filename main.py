import sys
from stats import get_word_count
from stats import get_char_count
from stats import sorted_dicts

def get_book_text(path):

    with open(path) as f:         # Open the file to be read
        contents = f.read()       # Read the contents of the file
    return contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])  # Get the book text from the command line argument
    count = get_word_count(contents)  # Get the word count
    count_msg = (f"Found {count} total words")
    letter_count = get_char_count(contents)  # Get the character count
    sorted_count = sorted_dicts(letter_count)  # Sort the character count
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(count_msg)
    print("--------- Character Count -------")
    for i in sorted_count:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")


    
main()


