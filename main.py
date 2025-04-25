from stats import count_words, stringify
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text =  get_book_text(book_path)
    chars = stringify(text)
    print(f'{len(count_words(text))} words found in the document')
    print(chars)
    
main()
