import string

# Function to generate text files
def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write(f"hello")
   

generate_text_files()
