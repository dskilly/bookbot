def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        return content
    
def get_num_words(book):
    text = get_book_text(book)
    return len(text.split())

def get_num_chars(book):
    text = get_book_text(book).lower()
    char_count = {}
    for c in text:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sort_list = []
    for i in dict:
        sort_list.append({"char": i, "num": dict[i]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list