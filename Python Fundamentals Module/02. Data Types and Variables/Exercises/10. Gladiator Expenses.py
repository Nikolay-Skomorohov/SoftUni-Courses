lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0
shield_broke = 0

for loss in range(1, lost_fights + 1):
    if loss % 2 == 0:
        total_cost += helmet_price
    if loss % 3 == 0:
        total_cost += sword_price
    if loss % 2 == 0 and loss % 3 == 0:
        total_cost += shield_price
        shield_broke += 1
        if shield_broke % 2 == 0:
            total_cost += armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")