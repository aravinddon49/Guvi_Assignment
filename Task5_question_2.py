# Define the number of levels in the pyramid
num_levels = 20

# Outer loop for each level
for i in range(1, num_levels + 1):
   # print(i)
    # Inner loop for each number in the current level
    for j in range(1, i + 1):
        #print(j)
        print(j, end=" ")  # Print the current number with a space
    print()  # Move to the next line after each level