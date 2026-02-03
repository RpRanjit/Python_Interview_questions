# Convert "Hello" into upper case "hello" without using in-built functions

user_input = input("Enter the word you want to convert into Uppercase: ")
result = ""

for char in user_input:
    if "A" <= char <= "Z":
        lower_char = chr(ord(char) +32)
        result += lower_char
    else:
        result += char
print(result)

# alternative method

result = []
for char in user_input:
    if  "A" <= char <= "Z":
        lower_char = chr(ord(char) + 32)
        result.append(lower_char)
    else:
        result.append(char)
print("".join(result))