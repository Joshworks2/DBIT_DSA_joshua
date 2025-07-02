def find_min(list):
    if len(list) == 0:
        return None

    min_value = list[0]
    for num in list[1:]:
        if num < min_value:
            min_value = num
    return min_value

# Example
numbers = [3, 7, 2, 5]
print("Min:", find_min(numbers))  # Output: Min: 2
