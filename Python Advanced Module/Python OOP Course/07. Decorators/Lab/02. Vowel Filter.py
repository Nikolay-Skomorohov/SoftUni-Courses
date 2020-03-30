def vowel_filter(function):
    def wrapper():
        result = list(filter(lambda x: x in ("a", "e", "i", "o", "u"),
                      function()))
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
