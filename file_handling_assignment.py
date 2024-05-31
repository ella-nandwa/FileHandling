# file_handling_assignment.py

# File Creation and Writing
try:
    with open("my_file.txt", 'w') as file:
        file.write("First line of text.\n")
        file.write("Second line with number: 12345.\n")
        file.write("Third line with another number: 67890.\n")
    print("File created and initial lines written successfully.")
except PermissionError:
    print("Error: Permission denied while writing to the file.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print("\nContents of the file after initial writing:")
        print(contents)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied while reading the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Fourth line appended.\n")
        file.write("Fifth line appended with a number: 54321.\n")
        file.write("Sixth line appended with another number: 98765.\n")
    print("Additional lines appended successfully.")
except PermissionError:
    print("Error: Permission denied while appending to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        contents = file.read()
        print("\nContents of the file after appending:")
        print(contents)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied while reading the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
