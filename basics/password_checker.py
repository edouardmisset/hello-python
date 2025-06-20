"""Password Checker"""

name = input('Name\n')
password = input('Password\n')
length: int = len(password)
masked_password: str = '*' * length

print(f'{name}, your password {masked_password} is {length} characters long')
