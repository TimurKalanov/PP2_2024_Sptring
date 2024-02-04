def unique(my_list):
    unique_list =[]
    for it in my_list:
        if it not in unique_list:
            unique_list.append(it)
    return unique_list
my_list = [1, 2 , 2, 4, 5, 6]
unique_list = unique(my_list)
print (unique_list)