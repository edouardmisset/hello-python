"""Ternary Operator"""

is_friend = True

# do_something_when_truthy if condition else do_something_when_false
can_message = "message allowed" if is_friend else "not allowed"

print(can_message)  # message allowed
