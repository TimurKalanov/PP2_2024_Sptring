import re
def email(string):
    pattern = r'[a-z]+@gmail.com'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

s = input()
print(email(s))