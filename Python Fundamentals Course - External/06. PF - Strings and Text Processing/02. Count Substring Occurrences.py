input_text = input().lower()
search_string = input().lower()

count_occurrences = 0
index_num = 0

while index_num != -1:
    index_num = input_text.find(search_string, index_num)
    if index_num is not -1:
        count_occurrences += 1
        index_num += 1

print(count_occurrences)
