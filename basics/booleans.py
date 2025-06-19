
"""Booleans"""

is_valid: bool = True

is_invalid: bool = False

if is_invalid:
    print('invalid')
elif is_valid:
    print('valid')


print(bool('True'))  # True
print(bool('False'))  # True
print(bool('Hi'))  # True
print(bool(1))  # True
print(bool(0))  # False

# Key points about Python booleans:
# 1. The built-in `bool` type has only two values: `True` and `False`.
# 2. Many objects have an "inherent truth value" (truthiness/falsiness). For
#    example, empty sequences (`[]`, `''`, `()`, `{}`) and `None` are considered
#    `False`, while non-empty ones are `True`.
# 3. You can use `and`, `or`, and `not` for boolean logic.
# 4. Boolean values are a subclass of `int`, so `True == 1` and `False == 0` evaluate to `True`.
# 5. Custom classes can define their truthiness by implementing the `__bool__` or `__len__` methods.
