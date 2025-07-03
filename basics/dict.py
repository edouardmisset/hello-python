"""Dictionary"""

dic: dict[str, int] = {
    'a': 1,
    'b': 2
}

print(dic['a'])  # 1

print(dic['c'])  # KeyError

# A dictionary is an **ordered** (since python 3.7) key-value pair

dic['c'] = 1
