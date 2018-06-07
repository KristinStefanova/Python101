from collections import deque


def deep_find(data, key):
    deq = deque()
    deq.append(data)

    while len(deq) != 0:
        d = deq.popleft()
        if type(d) is dict:
            for k in d.keys():
                if k == key:
                    return d[k]
                deq.append(d[k])
        if type(d) is list or type(d) is tuple:
            for el in d:
                deq.append(el)
    return None


def deep_find_all(data, key):
    deq = deque()
    deq.append(data)
    result = []
    while len(deq) != 0:
        d = deq.popleft()
        if type(d) is dict:
            for k in d.keys():
                if k == key:
                    result.append(d[k])
                deq.append(d[k])
        if type(d) is list or type(d) is tuple:
            for el in d:
                deq.append(el)
    return result


def deep_update(data, key, val):
    result = {}
    for k, v in data.items():
        result[k] = v
        if isinstance(v, dict):
            result[k] = deep_update(v, key, val)
        if isinstance(v, list) or isinstance(v, tuple):
            new = []
            for item in v:
                new.append(deep_update(item, key, val))
            result[k] = new
        if k == key:
            result[k] = val
    return result


def deep_apply(func, data):
    result = {}
    for key, value in data.items():
        result[func(key)] = value
        if isinstance(value, dict):
            result[func(key)] = deep_apply(func, value)
        if isinstance(value, list) or isinstance(value, tuple):
            new = []
            for item in value:
                new.append(deep_apply(func, item))
            if isinstance(value, tuple):
                result[func(key)] = tuple(new)
            else:
                result[func(key)] = new
    return result


def deep_compare(obj1, obj2):
    d1 = deque()
    d2 = deque()
    d1.append(obj1)
    d2.append(obj2)
    while len(d1) != 0:
        top1 = d1.popleft()
        top2 = d2.popleft()
        if top1 != top2:
            return False
        if type(top1) != type(top2):
            return False
        if type(top1) is dict:
            for k in top1.keys():
                if k not in top2.keys():
                    return False
                if top1[k] != top2[k]:
                    return False
                d1.append(top1[k])
                d2.append(top2[k])
        if type(top1) is list or type(top1) is tuple:
            if len(top1) != len(top2):
                return False
            for i, j in zip(top1, top2):
                d1.append(i)
                d2.append(j)
    return len(d1) == len(d2)


def inthere(ls, s):
    if s in ls:
        return True
    else:
        for thing in ls:
            if isinstance(thing, list):
                if inthere(thing, s):
                    return True
    return False


def traverse(o):
    if isinstance(o, list):
        for value in o:
            if isinstance(value, list):
                for subvalue in traverse(value):
                    yield subvalue
            else:
                yield value
    else:
        yield o


def check_list_without_nesting(schema, data):
    s = [False for item in data if type(item) is list]
    d = [False for key in data.keys() if type(data[key]) is dict]
    if all(s) and all(d):
        for key in data.keys():
            if key not in schema:
                return False
        for item in schema:
            if item not in list(data.keys()):
                return False
    return True


def schema_validator(schema, data):
    if not check_list_without_nesting(schema, data):
        return False
    deq = deque()
    deq.append(data)
    stack = traverse(schema)
    while len(deq) != 0:
        top = deq.popleft()
        if type(top) is dict:
            for key in top.keys():
                deq.append(top[key])
                if not inthere(schema, key):
                    return False
                new_value = next(stack)
                if key != new_value:
                    return False
    return True




# def schema_validator(schema, data):
#     deq = deque()
#     deq.append(data)
#     level_keys = [item for item in schema if type(item) is not list]
#     while len(deq) != 0:
#         top = deq.popleft()
#         if type(top) is dict:
#             if len(list(top.keys())) < len(level_keys):
#                 return False
#             for key in top.keys():
#                 if key in level_keys:
#                     continue
#                 else:
#                     level_keys = [item[1] for item in schema if key in item]
#                     if level_keys == []:
#                         return False
#                     else:
#                         level_keys = level_keys[0]
#                 if type(top[key]) is dict:
#                     deq.append(top[key])
#     return True

two = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', ['inner_inner_key1', 'inner_inner_key2']]
    ]
]

dict_two = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': {
            'inner_inner_key1': 'in_val1',
            'inner_inner_key2': 'in_val2',
        }
    }
}

# data = {
#     'z': {
#         'b': {'a': 1}
#     },
#     'x': [
#         {'y': 3, 'z': 4}, {'d': {'a': 5}}
#     ],
#     'q': (
#         {'y': 6, 'z': 7},
#         {'y': 8, 'z': 9}
#     )
# }

# data2 = {
#     'a': {
#         'b': [
#             {'a': 1}, {'d': {'a': 5}}
#         ]
#     },
#     'x': [
#         {'y': 3, 'z': 4}
#     ],
#     'q': (
#         {'y': 6, 'z': 7},
#         {'y': 8, 'z': 9}
#     )
# }


# def dummy(ch):
#     return ord(ch)


schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', 'inner_key2']
    ]
]

data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    }
}

data2 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'not expected'
}

one = ['key1', 'key2']
dict_one = {'key1': 'val1'}

# print(deep_find(data, 'a'))
# print(deep_find_all(data, 'a'))
# print(deep_update(data, 'z', 25))
# print(schema, data)
# print(deep_apply(str.upper, data))
# print(data)
# print(deep_compare(data, data2))
# print(list(zip(schema, data.items())))
# print("\n------------\n", schema_validator(schema, data))
# print("\n------------\n", schema_validator(schema, data2))
# print("\n------------\n", schema_validator(one, dict_one))
# print("\n------------\n", schema_validator(two, dict_two))
