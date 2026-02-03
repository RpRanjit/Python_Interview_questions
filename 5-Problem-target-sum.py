# Finding a pair with a given sum in a sorted array

# 1. Start with one pointer at the begining (left) and another at the end (right)
# 2. Check the sum of values of these pointer:
#     -If the sum is equal to the target, return the pair
#      -If the sum is smaller than the target, move the left pointer to the right(increment by 1)
#      -If the sum is larger than the target, move the right pointer to the left(decrement by 1)
# 3. Continue until the two pointrs meet or you find a valid pair


def pair_sum_target(arr, target):
    left = 0
    right = len(arr) -1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return arr[left], arr[right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return None
arr = [1,2,3,4,6]
target = 5
print(pair_sum_target(arr, target))