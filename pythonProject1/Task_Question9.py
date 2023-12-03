def count_words(input_string):
    words = input_string.split()
    return len(words)

# Example usage:
input_string = "India is my country."
word_count = count_words(input_string)
print(f"The number of words in '{input_string}' is: {word_count}")
