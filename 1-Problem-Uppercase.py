# Convert "hello" into upper case "HELLO" without using in-built functions

user_choice = input("Enter the word you want to convert into Uppercase: ")


result = "" 
for char in user_choice:
    if "a" <= char <= "z":
        upper_char = chr(ord(char) - 32)
        result += upper_char
    else:
        result += char

print(result)

# Alternative
result = []
for char in user_choice:
    if "a" <= char <= "z":
        upper_char = chr(ord(char) -32)
        result.append(upper_char)
    else:
        result.append(char)
print("".join(result))