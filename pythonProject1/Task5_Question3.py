def remove_vowels(input_string):
    vowels = "AEIOUaeiou"
    result_string = ""

    for char in input_string:
        if char not in vowels:
            result_string += char

    return result_string

# Example usage:
input_string = "Hi, my name is Aravind"
result = remove_vowels(input_string)
print("Original String:", input_string)
print("String with Vowels Removed:", result)
