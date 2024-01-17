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

# Get the file name from the user or you can provide it directly
file_name = input("Enter the name of the text file: ")
read_text_file(file_name)
