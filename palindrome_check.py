def palindrome_check(strings):
    result = []
    for string in strings:
        # Normalize the string by making it lowercase and removing spaces
        normalized_string = string.lower().replace(" ", "")
        # Check if the string is the same forwards and backwards
        is_palindrome = normalized_string == normalized_string[::-1]
        result.append((string, is_palindrome))
    return result
strings = ["racecar", "hello", "madam", "step on no pets", "python"]
output = palindrome_check(strings)
print(output)