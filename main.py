from stats import word_count, string_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    words = word_count(text)
    character_count = string_character_count(text)
    print(f"{words} words found in the document")
    print(f"{character_count} in the document")
    

main()