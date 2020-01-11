items_list = input().split("|")
budget = float(input())
item_prices = []
profit = 0
revenue = 0

for item in items_list:
    valid = None
    current_item = item.split("->")
    if current_item[0] == "Clothes" and float(current_item[1]) <= 50.00:
        valid = True
    elif current_item[0] == "Shoes" and float(current_item[1]) <= 35.00:
        valid = True
    elif current_item[0] == "Accessories" and float(current_item[1]) <= 20.50:
        valid = True
    if valid is True:
        if budget - float(current_item[1]) >= 0:
            budget -= float(current_item[1])
            item_prices.append(float(current_item[1]) * 1.40)
            revenue += float(current_item[1]) * 1.40
            profit += ((float(current_item[1]) * 1.40) - float(current_item[1]))
budget += profit + revenue
for tag in item_prices:
    print(f"{tag:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")