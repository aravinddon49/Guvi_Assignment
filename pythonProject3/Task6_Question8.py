def find_minimum_element(sorted_list):
    if not sorted_list:
        return None  # Return None for an empty list

    return sorted_list[0]

# Example usage:
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
min_element = find_minimum_element(sorted_numbers)

if min_element is not None:
    print(f"The minimum element in the sorted list is: {min_element}")
else:
    print("The list is empty.")
