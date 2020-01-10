budget = float(input())
flour_price = float(input())
egg_pack_price = flour_price * 0.75
milk_price = flour_price * 1.25
cozcozonac_price = flour_price + egg_pack_price + (milk_price * 0.25)

cozonacs_count = 0
coloured_eggs_count = 0

while (budget - cozcozonac_price) > 0:
    budget -= cozcozonac_price
    cozonacs_count += 1
    coloured_eggs_count += 3
    if cozonacs_count % 3 == 0:
        coloured_eggs_count -= (cozonacs_count - 2)

print(f"You made {cozonacs_count} cozonacs! Now you have {coloured_eggs_count} eggs and {budget:.2f}BGN left.")
