from stats import count_words, characters_count
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
        print(f"Analyzing book found at {path_to_file}...")
        contents =  f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for k,v in (characters_count(book_text)).items():
        print(f"'{k}: {v}'")
    print("============= END ===============")
main()