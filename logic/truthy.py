"""Truthy and Falsy"""

print(bool(5))  # True
print(bool('hi'))  # True

print(bool(""))  # False
print(bool(0))  # False
print(bool(None))  # False
print(bool(False))  # False
print(bool(0.0))  # False
print(bool(0j))  # False
print(bool(set[int]()))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool((b'')))  # False
print(bool((range(0))))  # False

password = "123"
user = "john"

# This is type coercion
if user and password:
    print('You can login')
