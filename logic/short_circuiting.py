"""Short circuiting evaluation in logical operations"""


is_friend = True
is_user = True

if is_friend and is_user:
    print('BFF')

# BFF

is_friend = False

# Short-circuited `is_user` because `is_friend`  is False
if is_friend or is_user:
    print('Hello user')
    # Prints "Hello user"

# Short-circuited `is_user` because `is_friend` is False
if is_friend and is_user:
    print('Hello user friend')
    #  Doesn't print
