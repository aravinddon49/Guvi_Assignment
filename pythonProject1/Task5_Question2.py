# Define the number of rows in the pyramid
num_rows = 20

# Loop to iterate over each row
for i in range(1, num_rows + 1):
    # Print spaces before the numbers
    print(" " * (num_rows - i), end="")

    # Print numbers in increasing order
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line after each row
    print()



