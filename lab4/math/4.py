def area_of_parallelogram(base_length, height):
    area = base_length * height
    return area
base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = area_of_parallelogram(base_length, height)

print("Expected Output:", parallelogram_area)
