def first_non_repeating_element(nums):
    for num in nums:
        # Check if the current element appears only once in the list
        if nums.count(num) == 1:
            return num

    # If no non-repeating element is found
    return None

# Example usage:
numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
result = first_non_repeating_element(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found.")
