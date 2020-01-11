input_string = input().split("#")
water = int(input())
result = []
effort = 0
total_fire = 0

for fire in input_string:
    valid = None
    current_fire = fire.split(" = ")
    if current_fire[0] == "High" and int(current_fire[1]) in range(81, 126):
        valid = True
    elif current_fire[0] == "Medium" and int(current_fire[1]) in range(51, 81):
        valid = True
    elif current_fire[0] == "Low" and int(current_fire[1]) in range(1, 51):
        valid = True
    if water - (int(current_fire[1])) >= 0 and valid is True:
        water -= (int(current_fire[1]))
        effort += (int(current_fire[1]) * 0.25)
        total_fire += (int(current_fire[1]))
        result.append(current_fire[1])

print("Cells:")
for cell in result:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


