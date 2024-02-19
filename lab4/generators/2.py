def generate_even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

def he():
    n_input = input("number: ")
    if not n_input.isdigit():
        print("need correct")
        return
    n = int(n_input)
    if n < 0:
        print("more than")
        return
    even_numbers = list(generate_even_numbers(n))
    print("even number from 0 to {}: {}".format(n, ', '.join(map(str, even_numbers))))

he()
