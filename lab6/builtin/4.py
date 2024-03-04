import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result


input_number = int(input("number: "))
input_milliseconds = int(input("milliseconds: "))
    
result = calculate_square_root(input_number, input_milliseconds)
print(f"Square root of {input_number} after {input_milliseconds} milliseconds is {result}")