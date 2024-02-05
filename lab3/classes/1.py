class string:
    def __init__(self):
        self.my_string =""
    def getString(self):
        self.my_string = input()
    def printString(self):
        print (self.my_string.upper())
my_string_obj = string()
my_string_obj.getString()
my_string_obj.printString()