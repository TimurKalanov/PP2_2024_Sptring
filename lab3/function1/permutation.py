from itertools import permutations
def permu(string):
    perms = permutations(string)
    for perm in perms:
        print (''.join(perm))
my_input = input()
permu(my_input)