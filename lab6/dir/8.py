import os
def delete_file(file_path):
 
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if not os.access(file_path, os.R_OK | os.W_OK):
        print("Permission denied to access the file.")
        return

    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")


file_path = input("Enter the path of the file you want to delete: ")
delete_file(file_path)