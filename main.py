from stats import get_number_of_words, get_character_counts, get_sorted_character_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

    
def main():
    
    
    if (len(sys.argv) > 1):
        book_path = sys.argv[1] if len(sys.argv) > 1 else None
        book_text = get_book_text(book_path)
    else:
        print("Please provide the path to the book you want to analyze as a command line argument with \"Usage: python3 main.py <path_to_book>\".\nFor example: python main.py books/frankenstein.txt")
        exit(1)
    
    # print("Let's analyze a book together!\nPlease provide the path to the book you want to analyze as a command line argument.\nFor example: python main.py books/frankenstein.txt")
    # input= input("Press Enter to continue...")
    
    num_words = get_number_of_words(book_text)
    num_characters = get_character_counts(book_text)
    sorted_character_counts = get_sorted_character_counts(num_characters)


    # beginning of structured report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at 'books/{book_path}'...")
    print("----------- Word Count ----------")
    # Print the number of words in the book
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Print the number of times each character appears in the book
    for char, count in sorted_character_counts:
        print(f"{char}: {count}")
    print("============= END ===============")
    
main()