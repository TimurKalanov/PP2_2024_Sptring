def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

start = 1
end = 5

print(f"Squares from {start} to {end}:")
for square in squares(start, end):
    print(square)
