def function():
    n = int(input())
    ranges = []
    result = []
    [ranges.append(input()) for x in range(n)]
    for rng in ranges:
        first_part = rng.split("-")[0].split(",")
        second_part = rng.split("-")[1].split(",")
        first_range = set([x for x in range(int(first_part[0]), int(first_part[1]) + 1)])
        second_range = set([x for x in range(int(second_part[0]), int(second_part[1]) + 1)])
        result.append(first_range.intersection(second_range))

    return f"Longest intersection is {list(max(result, key=len))} with length {len(max(result, key=len))}"


print(function())
