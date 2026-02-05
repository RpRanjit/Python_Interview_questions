def char_count(word):
    word_dict = {}
    compressed_word = ""
    list = []
    for char in word:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    for char, values in word_dict.items():
        list.append(f"{char}{values}")
    return "".join(list)
print(char_count("paraparo"))