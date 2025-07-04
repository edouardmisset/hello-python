"""Set"""

# Unordered collection of unique 'things'

my_set = {1, 2, 3, 4, 5, 5, 5, 5}
print(my_set)  # {1, 2, 3, 4, 5}

my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

my_set.add(100)
print(my_set)  # {1, 2, 3, 4, 5, 100}

my_list = [1, 2, 3, 4, 5, 5, 5, 5]
new_set = set(my_list)
print(new_set)  # {1, 2, 3, 4, 5}

# Accessing

print(1 in my_set)  # True
print(len(my_set))  # 6, because 100 was added

newer_set = my_set.copy()
my_set.clear()

print(my_set)  # set()
print(newer_set)  # {1, 2, 3, 4, 5, 100}

# Set theory and their methods

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))  # {1, 2, 3}
print(my_set.discard(5))  # None
print(my_set)  # {1, 2, 3, 4}

my_set = {1, 2, 3, 4, 5}

print(my_set.difference_update(your_set))  # None => changes the set
print(my_set)  # {1, 2, 3}

my_set = {1, 2, 3, 4, 5}

print(my_set.intersection(your_set))  # {4, 5}
print(my_set & your_set)  # {4, 5}

print(my_set.isdisjoint(your_set))  # False
# these sets have at least one element in common

print(my_set.union(your_set))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Subset
print(my_set.issubset(your_set))  # False
print({5, 6}.issubset(your_set))  # True

# Superset

print(my_set.issuperset(your_set))  # False
print({1, 2, 3, 4, 5}.issuperset(my_set))  # True
