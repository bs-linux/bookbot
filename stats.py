def get_word_count(contents):
    words = contents.split()      # Split the contents into words
    word_count = len(words)      # Count the number of words
    return word_count

def get_char_count(contents):
    contents = contents.lower()  # Convert to lowercase at the very beginning
    char_count = {}
    for char in contents:
        if char.isalpha() and char >= 'a' and char <= 'z':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_dicts(char_count):
    sorted_stuff = list(char_count.items())
    sorted_stuff.sort(key=lambda x: x[1], reverse=True)
    sorted_by_value = [{"char": char, "num": num} for char, num in sorted_stuff]
    return sorted_by_value
