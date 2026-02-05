# Write a Python Function that compresses a given string by replacing sequences of the same character by the character followed by the count.if the compressed string is not smaller that the original string, return the original string.



def string_compressed(s):
    compressed_char = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed_char.append(s[i-1] + str(count))
            count = 1
    compressed_char.append(s[-i] + str(count))

    compressed_string = "".join(compressed_char)
        
    if len(compressed_string) > len(s):
        return s
    else:
        return compressed_string
print(string_compressed("ppaaapp"))
    
