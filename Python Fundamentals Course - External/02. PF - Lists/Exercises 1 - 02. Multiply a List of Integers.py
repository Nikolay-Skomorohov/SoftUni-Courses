list_floats = list(map(int, input().split()))
multi_float = float(input())

list_floats = [int(i * multi_float) for i in list_floats]

print(*list_floats)
