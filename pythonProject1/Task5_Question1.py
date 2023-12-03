def count_vowels(string):
    # Convert the string to lowercase to make the count case-insensitive
    string = string.lower()

    # Initialize counts for total vowels and each individual vowel
    total_vowels = sum(1 for char in string if char in 'aeiou')
    individual_vowel_counts = {vowel: string.count(vowel) for vowel in 'aeiou'}

    return total_vowels, individual_vowel_counts

# Given string
input_string = "Guvi Geeks Network Private Limited"

# Call the function and print the results
total_vowels, individual_vowel_counts = count_vowels(input_string)

print("Original String:", input_string)
print("Total Number of Vowels:", total_vowels)
print("Count of Each Individual Vowel:", individual_vowel_counts)
