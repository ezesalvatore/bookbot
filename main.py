import sys

from stats import get_num_words, get_dict

def get_book_text(f):
    with open(f) as f:
        file__contents = f.read()
    return file__contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    file_name = sys.argv[1]
    print(f"Analyzing book found at {file_name}...")
    book = get_book_text(file_name)

    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

    print("---------- Character Count -------")
    occurance = get_dict(book)
    sorted_occurance = dict(sorted(occurance.items(), key=lambda x: x[1], reverse=True))
    for key, val in sorted_occurance.items():
        print(f"{key}: {val}")

    print("============= END ===============")

    print("I'm back")
    
main()