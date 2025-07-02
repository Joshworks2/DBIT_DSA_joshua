def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

# Example
numbers = [3, 7, 2, 5]
target = 2
print("Index of", target, ":", linear_search(numbers, target))  # Output: Index of 2 : 2
