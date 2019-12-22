banned_words_list = input().split()
text_input = input()

for word in banned_words_list:
    if word in text_input:
        replace_with = "*" * len(word)
        text_input = text_input.replace(word, replace_with)

print(text_input)
