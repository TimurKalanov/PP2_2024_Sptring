import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians

input_degree = float(input("Input degree: "))
radian = degree_to_radian(input_degree)
print(radian)
