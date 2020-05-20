# define a doubling function that passes args by value

def double(x):
    return x * 2

num = 10
num = double(num)
print(num)

# define a doubling function that doubles every element in a list
# the argument is passed by reference

def double_list(li):
    # to make this immutable use list comprehension new_list = [element * 2 for element in li]
    for i in range(0, len(li)):
        li[i] *= 2
    return li
    # return new_list

num_list = [1,2,3,4,5]
print(num_list)
double_list(num_list)
print(num_list)

# pass a collection by value
import copy
num_list = [1,2,3,4,5]
print(num_list)
num_list = double_list(copy.copy(num_list))
print(num_list)