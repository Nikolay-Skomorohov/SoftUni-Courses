input_list = [int(x) for x in input().split(" ")]
positive_list = list(filter(lambda x: x >= 0, input_list))
negative_list = list(filter(lambda x: x < 0, input_list))
new_negative_list = list(map(abs, negative_list))
print(sum(negative_list))
print(sum(positive_list))
if sum(new_negative_list) > sum(positive_list):
    print(f"The negatives are stronger than the positives")
elif sum(new_negative_list) < sum(positive_list):
    print(f"The positives are stronger than the negatives")
