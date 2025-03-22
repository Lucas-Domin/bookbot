from stats import word_count, string_character_count, dictionary_to_list_sorted

book_path = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        return f.read()

def main():
    text = get_book_text(book_path)
    words = word_count(text)
    character_count = string_character_count(text)
    dict_list = dictionary_to_list_sorted(character_count)

    print(f"""
=========== BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")

    for k, v in dict_list:
        print(f"{k}: {v}")

main()