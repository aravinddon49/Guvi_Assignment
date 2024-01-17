def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Provide the file name directly
file_name = "example.txt"  # Replace with your file name
read_text_file(file_name)
