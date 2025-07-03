"""Dictionary"""

# A dictionary is an **ordered** (since python 3.7) key-value pair

my_dict: dict[str, int] = {
    'a': 1,
    'b': 2
}

print(my_dict['a'])  # 1

# print(my_dict['c'])  # KeyError

my_dict['c'] = 1

my_dic2: dict[object, object] = {
    123: [1, 2, 3],
    True: 'yes',
    'true': True
}

print(my_dic2)

# Keys must be unique

user: dict[object, object] = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

# Method

# weekend can use a getter with a "default value" / "fallback value"
age = user.get('age', 25)

print(age)  # 25

print("greet" in user)  # True
print("age" in user)  # False

print("hello" in user.values())  # True

print(user.items())  # dict_items([('basket', [1, 2, 3]), ('greet', 'hello')])

user2 = user.copy()

user.clear()

print(user)  # {}
print(user2)  # {'basket': [1, 2, 3], 'greet': 'hello'}

print(user2.pop('greet'))  # hello
print(user2.popitem())  # As of 3.7, it removes the last key-value pair

print(user2.update({'greet': 'hi'}))
print(user2)  # {'greet': 'hi'}
