
"""Built in functions and methods"""

print(len('12345'))  # 5

greet: str = 'hello'

print(greet[0:len(greet)])  # hello

print(greet.upper())  # HELLO
print(greet.capitalize())  # Hello
print(greet.find('l'))  # 2 ('l' is present in the string at index 2)
print(greet.replace('l', 'r'))  # herro (replaces all the instances)
print(greet)  # hello as strings are immutable

# 1: len() | Returns the number of items in an object (e.g., string, list,
# tuple, etc.)
# 2: print() | Outputs data to the standard output (console)
# 3: type() | Returns the type of an object
# 4: str() | Converts an object to a string
# 5: int() | Converts an object to an integer
# 6: float() | Converts an object to a floating point number
# 7: input() | Reads a line of input from the user
# 8: list() | Creates a list from an iterable
# 9: dict() | Creates a dictionary
# 10: range() | Generates a sequence of numbers
