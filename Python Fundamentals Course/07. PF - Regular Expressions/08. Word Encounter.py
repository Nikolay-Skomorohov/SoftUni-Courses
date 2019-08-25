import re

sentence_pattern = r"[A-Z].*[!.?]+"
word_pattern = r"(\b[\w]+\b)"
symbols_input = input()
symbol = symbols_input[0]
number = int(symbols_input[1])
command = input()
to_print_list = []

while command != 'end':
    if re.fullmatch(sentence_pattern, command):
        word_list = re.findall(word_pattern, command)
        for word in word_list:
            if word.count(symbol) >= number:
                to_print_list.append(word)
    command = input()

print(", ".join(to_print_list))