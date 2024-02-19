import math

def area_of_regular_polygon(num_sides, side_length):

    angle_in_radians = math.radians(180 / num_sides)
    
    area = (num_sides * side_length ** 2) / (4 * math.tan(angle_in_radians))
    
    return area

num_sides = int(input("number of sides: "))

side_length = float(input("Input the length of a side: "))

polygon_area = area_of_regular_polygon(num_sides, side_length)

print("The area of the polygon :", polygon_area)
