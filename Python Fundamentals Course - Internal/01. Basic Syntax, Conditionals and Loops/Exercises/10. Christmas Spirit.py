allowed_quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_cost = 0
gained_spirit = 0
day_number = 0


while days_left > 0:
    brought = None
    day_number += 1
    if day_number % 11 == 0:
        allowed_quantity += 2
    if day_number % 2 == 0:
        total_cost += allowed_quantity * ornament_set_price
        gained_spirit += 5
    if day_number % 3 == 0:
        total_cost += (allowed_quantity * tree_skirt) + (allowed_quantity * tree_garland)
        gained_spirit += 13
        brought = True
    if day_number % 5 == 0:
        total_cost += allowed_quantity * tree_lights
        gained_spirit += 17
    if day_number % 10 == 0:
        total_cost += tree_lights + tree_garland + tree_skirt
        gained_spirit -= 20
    if day_number % 10 == 0 and days_left == 1:
        gained_spirit -= 30
    if brought and day_number % 5 == 0:
        gained_spirit += 30
    days_left -= 1

print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")

# while days_left > 0:
#     day_number += 1
#     if day_number % 2 == 0:
#         total_cost += allowed_quantity * ornament_set_price
#         gained_spirit += 5
#         if day_number % 3 == 0:
#             total_cost += (allowed_quantity * tree_skirt) + (allowed_quantity * tree_garland)
#             gained_spirit += 13
#         if day_number % 5 == 0:
#             total_cost += allowed_quantity * tree_lights
#             gained_spirit += 17
#         if day_number % 10 == 0:
#             total_cost += tree_lights + tree_garland + tree_skirt
#             gained_spirit -= 20
#             if days_left == 1:
#                 gained_spirit -= 30
#     elif day_number % 2 == 1:
#         if day_number % 3 == 0:
#             total_cost += (allowed_quantity * tree_skirt) + (allowed_quantity * tree_garland)
#             gained_spirit += 13
#         if day_number % 5 == 0:
#             total_cost += (allowed_quantity * tree_lights)
#             gained_spirit += 17
#             if day_number % 3 == 0:
#                 gained_spirit += 30
#         if day_number % 11 == 0:
#             allowed_quantity += 2
#     days_left -= 1