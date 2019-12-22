input_word = input()

new_word = ""

counter = len(input_word)

for x in range(len(input_word) - 1, -1, -1):
    new_word += input_word[x]

print(new_word)