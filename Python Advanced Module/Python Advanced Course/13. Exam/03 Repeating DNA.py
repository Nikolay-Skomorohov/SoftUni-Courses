def get_repeating_DNA(test):
    the_string = list(test)
    result = []
    to_check = None
    for index in range(0, len(the_string)):
        to_check = the_string[index:index + 10]
        if len(to_check) < 10:
            break
        for i in range(index + 1, len(the_string)):
            new_string = the_string[i:i + 10]
            if len(new_string) < 10:
                break
            if to_check == new_string:
                if not "".join(new_string) in result:
                    result.append("".join(new_string))
    return result

print(get_repeating_DNA("AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"))
print(get_repeating_DNA("TTCCTTAAGGCCGACTTCCAAGGTTCGATC"))
print(get_repeating_DNA("AAAAAAAAAAA"))