"""Lists"""

number_list = [1, 2, 3, 4, 5, 6]  # basic list syntax
string_list = ["a", "b", "c"]  # list of strings

# Lists in python are like arrays in Javascript

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

# List work (like in JS) with pointer. That is, if you assign a list to another
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

