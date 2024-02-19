def divisible_by_three_and_four(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
generator = divisible_by_three_and_four(n)
print("Numbers divisible by both 3 and 4 between 0 and {}: {}".format(n, list(generator)))
