words_list = input().split()

results = []
for word in words_list:
    if word == word[::-1]:
        if word in results:
            pass
        else:
            results.append(word)


results.sort(key=str.lower)

print(*results, sep=", ", end="")