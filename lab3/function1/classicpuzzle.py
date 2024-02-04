def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        if numrabbits * 4 + numchickens * 2 == numlegs:
            return numrabbits, numchickens
x = 35
y = 94
z = solve(x, y)

print ( z )
