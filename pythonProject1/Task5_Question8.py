def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str1 = ''.join(str1.split()).lower()
    cleaned_str2 = ''.join(str2.split()).lower()

    # Check if the sorted characters of both strings are the same
    return sorted(cleaned_str1) == sorted(cleaned_str2)

# Example usage:
string1 = "cat"
string2 = "Act"
result = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")
