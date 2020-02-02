item_categories = {x: {} for x in input().split(", ")}

number = int(input())


for i in range(number):
    command = input().split(" - ")
    if command[0] in item_categories:
        if not command[1] in item_categories[command[0]]:
            q2 = [command[2].split(";")[0].split(":"), command[2].split(";")[1].split(":")]
            item_categories[command[0]][command[1]] = {x: int(y) for x, y in q2}
    else:
        pass

count_items = sum(sum(sum(p for z, p in y.items() if z == "quantity") for y in x.values()) for x in item_categories.values())
average_quality = sum(sum(sum(p for z, p in y.items() if z == "quality") for y in x.values()) for x in item_categories.values()) / len(item_categories)

print(f"Count of items: {count_items}")
print(f"Average quality: {average_quality:.2f}")
# print(*[f"{x} -> {k}" for k in y.keys() for x, y in item_categories.items()], sep="\n")
[print(f"{x} -> {', '.join(list(item_categories[x].keys()))}") for x in item_categories.keys()]
