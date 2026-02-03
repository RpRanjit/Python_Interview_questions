def reverse_string(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        # swaping characters at the left and right pointers
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        # Moving pointers towards the center
        left += 1
        right -= 1

    return ''.join(s)#Convert back to string
print(reverse_string("Hello"))


