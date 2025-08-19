from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict

def main():
    print("============ BOOKBOT ============")
    book = "books/frankenstein.txt"
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(book)
    # for c in num_chars:
    #     print(f"'{c}': {num_chars[c]}")
    new_list = sort_dict(num_chars)
    for c in new_list:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()