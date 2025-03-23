def word_count(text):
    words = text.split()
    return len(words)

def clean(text):
    cleaned = ""
    for char in text:
        if char.isalpha() and char.isascii(): # enforces standard english letters
            cleaned += char
    return cleaned

def string_character_count(text):
    text = clean(text.lower()) # lowercase for character count
    character_count = {}
    for i in text:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count

def dictionary_to_list_sorted(dictionary):
    dict_list = list(dictionary.items()) # convert to list 
    dict_list.sort(key=lambda x: x[1], reverse=True) # sort by countdesc
    return dict_list

