def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2

N = 5
for square in generate_squares(N):
    print(square)
