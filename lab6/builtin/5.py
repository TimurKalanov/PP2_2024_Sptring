def all_true_in_tuple(my_tuple):
    return all(my_tuple)

my_tuple = (True, True, False, True)
print(all_true_in_tuple(my_tuple))  

my_tuple = (True, True, True)
print(all_true_in_tuple(my_tuple))  
