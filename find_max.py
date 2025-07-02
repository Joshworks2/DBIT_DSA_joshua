def find_max(list):
    if len(list) == 0:
        return None
    
    max_value = list[0]
    for num in list[1:]:
        if num > max_value:
            max_value = num
    return max_value

# Example
numbers = [3, 7, 2, 5]
print("Max:", find_max(numbers))  # Output: Max: 7
