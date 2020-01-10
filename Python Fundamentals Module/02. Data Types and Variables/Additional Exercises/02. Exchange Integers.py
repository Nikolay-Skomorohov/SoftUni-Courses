a = int(input())
b = int(input())

temp_a = a
temp_b = b

a = temp_b
b = temp_a

print(f"Before:\n"
      f"a = {temp_a}\n"
      f"b = {temp_b}")
print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")