
def most_frequent_char(input_string):
    char_count = {}

    # Count occurrences of each character in the string
    for char in input_string:
        if char.isalpha():  # Consider only alphabetical characters
            char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum count
    most_frequent = max(char_count, key=char_count.get)

    return most_frequent

# Example usage:
input_string = "invigorating"
result = most_frequent_char(input_string)
print(f"The most frequent character in '{input_string}' is: {result}")