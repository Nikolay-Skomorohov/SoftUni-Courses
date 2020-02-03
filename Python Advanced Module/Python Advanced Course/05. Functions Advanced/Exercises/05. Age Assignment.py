def age_assignment(*args, **kwargs):
    result = {}
    names = list(args)
    for name in names:
        if name[0] in kwargs:
            result[name] = kwargs[name[0]]
    return result
