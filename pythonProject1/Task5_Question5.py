def is_palindrome(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Remove spaces from the string
    input_string = input_string.replace(" ", "")

    # Compare the original and reversed strings
    return input_string == input_string[::-1]

# Example usage
test_string = "Malayalam"
result = is_palindrome(test_string)

if result:
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")

#Replacing test_string value with "Tamil" will give negative result.
