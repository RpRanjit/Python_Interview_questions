# Moving all zeros at the end
def placing_zero_last(arr):
    non_zero_char = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[non_zero_char]
            arr[non_zero_char] = arr[i]
            arr[i] = temp
            non_zero_char += 1
    return arr
print(placing_zero_last([0,2,3,0,5,1,0]))

# Alternative

def placing_zero_last(arr):
    non_zero_char = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_char], arr[i] = arr[i], arr[non_zero_char]
            non_zero_char += 1
    return arr
print(placing_zero_last([0,2,3,0,5,1,0]))