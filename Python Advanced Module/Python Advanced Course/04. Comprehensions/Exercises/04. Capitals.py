countries_list = [x for x in input().split(", ")]
capitals_list = [x for x in input().split(", ")]

dict_result = [x for x in zip(countries_list, capitals_list)]

print(*[f"{x} -> {y}" for x, y in dict_result], sep="\n")

# print(*{f"{x} -> {y}" for x, y in zip([x for x in input().split(", ")], [x for x in input().split(", ")])}, sep="\n")

