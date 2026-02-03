def longest_word(sentence):
    char_list = sentence.split(" ")
    long_length = 0
    for i in range(len(char_list)):
        if len(char_list[i]) > long_length:
            long_length = len(char_list[i])
    return long_length, char_list[i]
        
print(longest_word("I love Python Programming"))
