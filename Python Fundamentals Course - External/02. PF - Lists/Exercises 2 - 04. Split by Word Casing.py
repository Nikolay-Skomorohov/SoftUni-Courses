separators = (",", ";", ":", ".", "!", "(", ")", '"', "'", "\\", "/", "[", "]")

text_input = input()

lower_case = []
mixed_case = []
upper_case = []

for sep in separators:
    text_input = list(text_input.split(sep))
    text_input = " ".join(text_input)
text_input = list(text_input.split(" "))

for new_word in text_input:
    if new_word.isupper() and new_word.isalpha():
        upper_case.append(new_word)
    elif new_word.islower() and new_word.isalpha():
        lower_case.append(new_word)
    elif new_word != "":
        mixed_case.append(new_word)


print(f"Lower-case: {', '.join(lower_case)}")
print(f"Mixed-case: {', '.join(mixed_case)}")
print(f"Upper-case: {', '.join(upper_case)}")
