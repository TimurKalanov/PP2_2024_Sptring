import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists!")
        
        
        directory, filename = os.path.split(path)
        
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")


path = input("Enter a path to check: ")
check_path(path)
