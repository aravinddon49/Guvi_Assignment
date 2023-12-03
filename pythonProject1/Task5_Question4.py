def count_unique_characters(input_string):
    # Use a set to store unique characters
    unique_characters = set()

    # Iterate through each character in the string
    for char in input_string:
        # Add the character to the set
        unique_characters.add(char)

    # Return the number of unique characters
    return len(unique_characters)

# Example usage
input_str = "ARAVIND"
result = count_unique_characters(input_str)
print(f"The number of unique characters in '{input_str}' is: {result}")
