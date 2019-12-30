input_string = input().lower()

word_list = ["sand", "water", "fish", "sun"]

count = 0

for word in word_list:
    if word in input_string:
        count += input_string.count(word)
print(count)
