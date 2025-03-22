def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)


def main():
    text = get_book_text("books/frankenstein.txt")
    words = word_count(text)
    print(f"{words} words found in the document")
    

main()