"""Type Conversion"""

import datetime

birth_year = input('What year were you born?\n')

# print(birth_year)
# print(type(birth_year))

age: int = datetime.datetime.now().year - int(birth_year)

print(f'Your age is {age}')
