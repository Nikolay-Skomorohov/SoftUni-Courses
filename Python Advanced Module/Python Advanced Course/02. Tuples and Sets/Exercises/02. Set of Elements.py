numbers = [int(x) for x in input().split(" ")]

n, m = numbers

numbers = n + m

set1 = set([input() for x in range(n)])
set2 = set([input() for x in range(m)])

result = set1 & set2
[print(x) for x in result]