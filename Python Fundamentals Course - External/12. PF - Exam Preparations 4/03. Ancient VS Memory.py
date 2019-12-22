import re


def check_with_regex(new_line: str):
    words_list = []
    pattern_regex = r"(?P<start>32656 19759 32763)( 0 (?P<size>\d{1,}) 0 )(?P<rest>.*?)(?=32656|$)"
    for match in re.finditer(pattern_regex, new_line):
        iter_num = int(match.group('size'))
        num_list = list(match.group('rest').split())
        new_word = ""
        for ch in range(iter_num):
            new_word += chr(int(num_list[ch]))
        words_list.append(new_word)
    return words_list


def print_result(words_list: list):
    for word in words_list:
        print(word)


def main():
    code_list = ""
    while True:
        new_line = input()
        if new_line == "DEBUG":
            break
        else:
            code_list += new_line + " "
    words_list = check_with_regex(code_list)
    print_result(words_list)


if __name__ == "__main__":
    main()
