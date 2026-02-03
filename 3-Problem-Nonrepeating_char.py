# def non_repeating_character(word):
#     char_count = {}

#     for s in word:
#         if s in char_count:
#             char_count[s] += 1
#         else:
#             char_count[s] = 1
#     for i in range(len(word)):
#         if char_count[word[i]] == 1:
#             return i
        
#     return -1
# print(non_repeating_character("swiss"))






def first_non_repetive_char(word):
    new_dict = {}
    for char in word:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    for i in range(len(word)):
        if new_dict[word[i]] == 1:
            return i
    return -1
print(first_non_repetive_char("aaab"))