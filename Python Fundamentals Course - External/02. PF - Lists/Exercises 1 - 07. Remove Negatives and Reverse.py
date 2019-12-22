list_nums = list(map(int, input().split()))
list_nums = list((filter(lambda x: x > 0, list_nums)))
list_nums.reverse()

if len(list_nums) < 1:
    print("empty")
else:
    print(*list_nums)
