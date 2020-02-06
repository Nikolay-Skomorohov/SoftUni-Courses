input_list =[x for x in input().split(" ")]
num_list = list(filter(lambda x: x.isdigit(), input_list))
num_list = list(map(int, num_list))
print_list = list(filter(lambda x: x > len(input_list), num_list))
print_list.sort()
print(*print_list)
