from datetime import datetime

def create_file_with_timestamp():
    # Generate current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a file with the timestamp
    file_name = f"timestamp_file_{current_timestamp}.txt"

    # Write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(current_timestamp)

    print(f"File created with the current timestamp: {current_timestamp}")

# Call the function to create the file
create_file_with_timestamp()
