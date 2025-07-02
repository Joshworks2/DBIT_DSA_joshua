def has_duplicates(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False

# Example
numbers = [3, 7, 2, 5, 3]
print("Has duplicates:", has_duplicates(numbers))  # Output: Has duplicates: True
