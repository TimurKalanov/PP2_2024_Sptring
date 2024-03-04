def readlinecount():
    with open(r"example.txt", "r") as file:
        lines = len(file.readlines())
        print("Total Number of lines:", lines)
readlinecount()