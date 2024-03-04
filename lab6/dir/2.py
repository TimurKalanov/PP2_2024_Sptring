import os

def check_access(path):
    # Check if path exists
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    # Check readability
    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable.")
    else:
        print(f"Path '{path}' is not readable.")

    # Check writability
    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable.")
    else:
        print(f"Path '{path}' is not writable.")

    # Check executability
    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable.")
    else:
        print(f"Path '{path}' is not executable.")


path = input("Enter the path to check: ")
check_access(path)
