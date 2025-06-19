"""Strings"""

print(type('hello there!'))  # str

# Multiline strings '''
long_string: str = '''
HELL
O
'''
print(long_string)


# Concatenation

first_name: str = 'Edouard'
last_name: str = 'Misset'

full_name: str = first_name + ' ' + last_name

print(full_name)  # Edouard Misset

# Type Conversion

print(type(int(str(100))))  # int => str => int

# Escape Sequences

weather: str = "It's sunny"
weather: str = 'It\'s sunny'  # Escape sequence "\"
back_slash: str = "\\"
tab: str = "\tsome code"
new_line: str = "\nNew line"

print(tab)
print(new_line)


# Formatted strings

name: str = 'Johnny'
age: int = 55

print('Hi ' + name + '. You are ' + str(age) + ' years old')
print('Hi {}. You are {} years old'.format(name, age))
print('Hi {0}. You are {1} years old'.format(name, age))
print('Hi {n}. You are {a} years old'.format(n="Sally", a=100))
print(f'Hi {name}. You are {age} years old')

# String indexes

# str[ start : end : step ]
# By default nothing for start means the first
# By default nothing for end means the last
# Negative indexes means from the other side / reverse

alpha: str = 'abcdefg'
c: str = alpha[2]
bd: str = alpha[1:4]
print(c)  # c
print(bd)  # bcd
print(alpha[0:6:1])  # abcdef
print(alpha[0:6:2])  # ace
print(alpha[0::2])  # aceg
print(alpha[::2])  # aceg
print(alpha[:5])  # abcde
print(alpha[-1])  # g
print(alpha[::-1])  # gfedcba
print(alpha[::-2])  # geca

# Immutability

# Strings in Python are immutable

hi: str = 'hi'
hi[0] = "B"  # pylint: disable=unsupported-assignment-operation
# => TypeError: 'str' object does not support item assignment
