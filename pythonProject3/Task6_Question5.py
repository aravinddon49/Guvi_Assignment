def minimize_difference(mango_counts, num_students):
    # Sort the list of mango counts in ascending order
    sorted_mango_counts = sorted(mango_counts)

    # Calculate the number of bags each student should get
    bags_per_student = len(sorted_mango_counts) // num_students

    # Calculate the remainder bags that need to be distributed
    remaining_bags = len(sorted_mango_counts) % num_students

    # Initialize variables to keep track of the minimum and maximum mango counts
    min_mangoes = float('inf')
    max_mangoes = float('-inf')

    # Iterate through each student and distribute bags
    for i in range(num_students):
        start_index = i * bags_per_student + min(i, remaining_bags)
        end_index = start_index + bags_per_student + (1 if i < remaining_bags else 0)

        # Update min and max mango counts
        min_mangoes = min(min_mangoes, min(sorted_mango_counts[start_index:end_index]))
        max_mangoes = max(max_mangoes, max(sorted_mango_counts[start_index:end_index]))

    # Calculate and return the difference
    difference = max_mangoes - min_mangoes
    return difference

# Example usage:
mango_counts = [5, 12, 7, 8, 15, 9, 20]
num_students = 3

result = minimize_difference(mango_counts, num_students)
print(f"The minimum difference in mango counts is: {result}")
