a = int(input())
b = int(input())
c = int(input())

if a < b:
    if b < c:
        print(c)
    else:
        print(b)
elif a > b:
    if a > c:
        print(a)
    else:
        print(c)