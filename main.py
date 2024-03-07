def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_char_list = get_sorted_char_list(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the book")
    print("")

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    letters = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def sort_key(dict):
    return dict["num"]


def get_sorted_char_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list


main()
