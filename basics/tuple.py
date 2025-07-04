"""Tuple"""

# Immutable lists

my_tuple = (1, 2, 3, 4)

# my_tuple[1] = 0  # TypeError 'my_tuple' does not support item assignment

print(4 in my_tuple)  # True

# Less flexible but more performant

# Can be keys of dictionaries

user = {
    (1, 2): [1, 2]
}


# Similar to lists, we can slice it

new_tuple = my_tuple[1:2]  # Remember, the end is exclusif

print(new_tuple)  # (2,)

print(my_tuple[0])  # 1
print(my_tuple[1])  # 2

x, y, z, *others = (1, 2, 3, 4, 5)

print(x)  # 1
print(y)  # 2
print(z)  # 3
print(others)  # [4, 5]

print(my_tuple.count(1))  # `1` is present once

print(my_tuple.index(4))  # `4` is at index 3 in the tuple

print(len(my_tuple))  # 4
