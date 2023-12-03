def sum_of_first_and_last_digit(number):
    # Convert the number to a string to easily extract digits
    num_str = str(number)

    # Get the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    # Calculate the sum
    result_sum = first_digit + last_digit

    return result_sum

# Example usage
user_input = int(input("Enter an integer: "))
result = sum_of_first_and_last_digit(user_input)
print(f"The sum of the first and last digit of {user_input} is: {result}")

