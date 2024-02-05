def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
numbers = [1,2,3,4,5,6,7,8,9,10,11]
prime_numbers = list(filter(lambda x: prime(x), numbers))
print (prime_numbers)
