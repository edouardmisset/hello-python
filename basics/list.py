"""Lists"""

number_list = [1, 2, 3, 4, 5, 6]  # basic list syntax
string_list = ["a", "b", "c"]  # list of strings

# Lists in Python are similar to arrays in JavaScript - both are ordered, mutable collections

# Indexing

print(number_list[0])  # 1
print(number_list[2])  # 3
print(string_list[-1])  # c

# List slicing

print(number_list[1:5:2])  # [2, 4]

# Lists are mutable

number_list[0] = 0

print(number_list)

# ...but list slicing creates a new list

new_number_list = number_list[:]  # creates a copy of the original list

new_number_list[0] = 10

print(new_number_list)  # [10, 2, 3, 4, 5, 6]
print(number_list)  # [0, 2, 3, 4, 5, 6]

# List work (like in JS) with reference. That is, if you assign a list to another
# one, you assign its reference not the values.

new_number_list = number_list
new_number_list[0] = 100

print(new_number_list)  # [100, 2, 3, 4, 5, 6]
print(number_list)      # [100, 2, 3, 4, 5, 6]

# Matrix (multi-dimensional lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][0])  # 1
print(matrix[2][2])  # 9

# Methods

print(len(matrix))  # 3

# ADDING

basket = [1, 2, 3, 4, 5]
# `.append` changes the list in place. It doesn't return the result
basket.append(100)

print(basket)  # [1, 2, 3, 4, 5, 100]

# `.insert` also modifies the list in place
basket.insert(0, 101)

print(basket)  # [101, 1, 2, 3, 4, 5, 100]


# `.extend` also modifies the list in place. It doesn't return anything `None`.
basket.extend([200, 300, 400])  # [101, 1, 2, 3, 4, 5, 100, 200, 300, 400]

print(basket)

# REMOVING

pop = basket.pop()  # Can also take in an INDEX
# It returns the poped element

print(pop)  # 400

print(basket.pop(0))  # 101

# `.remove` works in place. It removes a specific value in a list.
print(basket.remove(1))  # None

print(basket)  # [2, 3, 4, 5, 100, 200, 300]

basket.clear()  # Removes all items

print(basket)  # []

# Other important methods

basket = ["a", "b", "c", "d", "e"]

print(basket.index("d"))  # 3

# print(basket.index("d", 0, 3))  # ValueError: 'd' is not in list

print('d' in basket)  # True
print('x' in basket)  # False

print('in' in 'I am in the house')  # True

print(basket.count('a'))  # 1

basket.append("a")

print(basket.count('a'))  # 2

print(basket)  # ['a', 'b', 'c', 'd', 'e', 'a']
# ['a', 'a', 'b', 'c', 'd', 'e']. Like `.toSorted` method in JS
print(sorted(basket))
print(basket)  # ['a', 'b', 'c', 'd', 'e', 'a']

basket.sort()  # Sort the list in place

print(basket)  # ['a', 'a', 'b', 'c', 'd', 'e']

basket.reverse()  # Reverses the basket in place

print(basket)  # ['e', 'd', 'c', 'b', 'a', 'a']

print(basket[::-1])  # New list revered ['a', 'a', 'b', 'c', 'd', 'e']

# Range

print(list(range(1, 10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(11)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Join

sentence: str = ' '.join(['hi', 'my', 'name', 'is', 'Bob'])

print(sentence.capitalize())  # Hi my name is bob

# List Unpacking

a, b, c, *others, f = ['a', 'b', 'c', 'd', 'e', 'f']

print(a)  # a
print(others)  # ['d', 'e']
print(f)  # f

# This is like the rest operator in JS
