def copy_file(source_file, destination_file):
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully!")

source_file = "A.txt"
destination_file = "C.txt"
copy_file(source_file, destination_file)
