def most_repeating_char(word):
    char_dict = {}
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    max_char = ""
    max_count =0
    for char, count in char_dict.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_count, max_char

print(most_repeating_char("anaconda"))
