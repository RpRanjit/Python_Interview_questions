# Write a function to checkis a string is a palindrome(reads the same forward and backword)
# Concepts you should know loops, two-pointer echnique.

def check_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(check_palindrome("madam"))