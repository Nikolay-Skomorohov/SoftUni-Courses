def tags(arg):
    def decorator(func):
        def wrapper(*txt):
            result = ""
            result += "<" + arg + ">"
            result += func(*txt)
            result += "</" + arg + ">"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
