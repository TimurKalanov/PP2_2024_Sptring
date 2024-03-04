def write_list_to_file(file_path, data):
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("List has been written to the file successfully.")

data = [1, 2, 3, 4, 5]  
file_path = input("Enter the path to the file: ")
write_list_to_file(file_path, data)

