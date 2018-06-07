def deep_find(data, key):
    for k, v in data.items():
        if k == key:
            return v
        if type(v) is dict:
            deep_find(v, key)
        if type(v) is list or type(v) is tuple:
            for d in v:
                deep_find(v, key)
