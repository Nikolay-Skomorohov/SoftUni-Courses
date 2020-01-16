def total_price(stuff, quantity):
    if stuff == "coffee":
        return 1.50 * quantity
    elif stuff == "water":
        return 1.00 * quantity
    elif stuff == "coke":
        return 1.40 * quantity
    elif stuff == "snacks":
        return 2.00 * quantity


stuff_input = input()
quantity_input = int(input())

print(f"{total_price(stuff_input, quantity_input):.2f}")
