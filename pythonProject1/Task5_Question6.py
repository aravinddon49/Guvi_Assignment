def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # Initialize a 2D table to store lengths of common suffixes
    table = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Variables to store the length and ending position of the longest common substring
    max_length = 0
    end_position = 0

    # Fill the table and track the length and ending position of the longest common substring
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_position = i
            else:
                table[i][j] = 0

    # Extract the longest common substring
    common_substring = str1[end_position - max_length: end_position]

    return common_substring

# Example usage
str1 = "Contract"
str2 = "Contradiction"
result = longest_common_substring(str1, str2)
print(f"The longest common substring between '{str1}' and '{str2}' is: '{result}'")





