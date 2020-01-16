def char_range(char1, char2):
    result = []
    for ch in range(char_1 + 1, char_2):
        result.append(chr(ch))
    return result


char_1 = ord(input())
char_2 = ord(input())

print(*char_range(char_1, char_2))

