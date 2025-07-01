def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq


result = count_char_frequencies("data structures and algorithms")
print(result)