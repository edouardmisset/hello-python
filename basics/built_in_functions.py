"""Built in functions and methods"""

print(len('12345'))  # 5

greet: str = 'hello'

print(greet[0:len(greet)])  # hello

print(greet.upper())  # HELLO
print(greet.capitalize())  # Hello
print(greet.find('l'))  # 2 ('l' is present in the string at index 2)
print(greet.replace('l', 'r'))  # herro (replaces all the instances)
print(greet)  # hello
