import math

width = float(input())
depth = float(input())
height = float(input())

num_barrels = int(input())
volume_to_fill = width * depth * height
volume_filled = 0
for barrel in range(num_barrels):
    b_radius = float(input())
    b_height = float(input())
    barrel_volume = math.pi * b_height * b_radius * b_radius
    volume_filled += barrel_volume
    if volume_to_fill <= volume_filled:
        print(f"Truck is full. {barrel} on board!")
        exit()
print(f"All barrels on board. Capacity left - {volume_to_fill - volume_filled:.2f}.")
