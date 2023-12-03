def find_triplet_with_sum(nums, target_sum):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target_sum:
                    return [nums[i], nums[j], nums[k]]

    return None  # Return None if no such triplet is found

# Example usage:
given_list = [10, 20, 30, 9]
target_value = 59

result_triplet = find_triplet_with_sum(given_list, target_value)

if result_triplet is not None:
    print(f"The triplet with sum {target_value} is: {result_triplet}")
else:
    print("No triplet found with the given sum.")
