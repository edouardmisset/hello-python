"""Conditional Logic"""

is_above_18: bool = True
is_licensed: bool = True

if is_licensed and is_above_18:  # `and` is the same as `&&` in JS
    print("Start your engine!")
elif not is_above_18:
    print('How did you get a license without being of age ?')
elif not is_licensed:
    print('Go and get your licence.')
else:
    print("You can't drive!")
