def read_and_write_file():
    try:
        # Asks the user for the filename to read
        input_filename = input("Enter the name of the file to read: ")
        
        # Attempts to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modifies the content (example: add line numbers to each line)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]
        
        # Asks the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content to: ")
        
        # Writes the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been successfully written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()

    