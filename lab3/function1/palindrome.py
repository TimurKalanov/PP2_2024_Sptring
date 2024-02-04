def palindrome(string):
    if string == string[::-1]:
        return True
    return False
x = input()
if (palindrome(x)):
    print("word is palindrome")
else: print("is not palindrome")