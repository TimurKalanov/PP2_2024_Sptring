def filter_prime(num):
    count = 0
    for i in range(2,num + 1):
        if num % i == 0:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
def filterr_prime(numbers):
    return [num for num in numbers if filter_prime(num)]
        
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filterr_prime(my_list))