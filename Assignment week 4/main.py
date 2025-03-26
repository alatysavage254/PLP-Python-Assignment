def read_and_modify_file():
    try:
        
        filename = input("Enter the filename to read: ")

        
        with open(filename, "r") as file:
            content = file.readlines()  

        
        modified_content = [line.upper() for line in content]

        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()
