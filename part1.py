# Hello, World!
# print("Hello, world!")


# declaring a variable
# name = "Austen"


# string concatenation
# print("Hello " + name)


# f-strings
# print(f'Hello, {name}')


# create a list with some numbers
# p = [10, 40, 30, 60, 'banana']


# add an element to p
# print(p)
# p.append(77)
# print(p)

# print all values in each list
# for number in p:
#     print(number)

# for (index, number) in enumerate(p):
#     print(f'Element at {index} is {number}')

# using list comprehensions...
# create a new list containing the squares of all values in 'numbers'

numbers = [1, 4, 9, 16, 25]
squares = [ num * num for num in numbers ]

# for num in numbers:
#     squares.append(num*num)
print(squares)


# create a new list containing only the even values of 'numbers'

evens = [ num for num in numbers if num % 2 == 0 ]

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
print(evens)


# create a new list containing only the names that start with 's'

names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)


# create an empty dictionary

new_dict = {}


# create a dictionary with at least two key : value pairs

food_dict = {
    'apple': 'is a fruit',
    'carrots': 'is a vegetable'
}

food_dict['cucumber'] = 'is maybe a vegetable?'


# access & print an element in the dictionary

chosen_food = 'apple'
print(food_dict[chosen_food])


# iterate through a dictionary

for key, value in food_dict.items():
    print(f'{key} {value}')


# Tuples, immuptable data type

tup = (1, 2, 3, 4)
# can also be written tup = 1, 2, 3, 4, 

for item in tup:
    print(item)


# Set, unordered, unindexed, no duplicates

fruit = {'apple', 'banana', 'cucumber'}

for item in fruit:
    print(item)


print('cucumber' in fruit)

if 'cucumber' in fruit:
    print("Pretty sure it's a vegetable")

if 'carrot' not in fruit:
    print("The world is predictable")