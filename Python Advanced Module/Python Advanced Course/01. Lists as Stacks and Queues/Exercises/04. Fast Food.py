from collections import deque


def fast_food():
    capacity = int(input())
    orders = deque([int(x) for x in input().split(" ")])
    print(max(orders))
    while orders:
        if (capacity - orders[0]) >= 0:
            capacity -= orders[0]
            orders.popleft()
        else:
            break

    if orders:
        print(f"Orders left: {' '.join(map(str, orders))}")
    else:
        print("Orders complete")


fast_food()
