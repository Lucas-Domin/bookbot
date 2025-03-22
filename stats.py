def word_count(text):
    words = text.split()
    return len(words)

def string_character_count(text):
    character_count = {}
    text = text.lower()
    for i in text:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count
