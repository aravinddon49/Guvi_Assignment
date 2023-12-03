def has_sublist_with_zero_sum(nums):
    running_sum = 0
    seen_sums = set()

    for num in nums:
        running_sum += num

        # Check if the current running sum has been seen before
        if running_sum in seen_sums or running_sum == 0:
            return True

        seen_sums.add(running_sum)

    return False

# Example usage:
given_list = [1, 2, -3, 1]

if has_sublist_with_zero_sum(given_list):
    print("There is a sub-list with sum equal to zero.")
else:
    print("No sub-list with sum equal to zero found.")

