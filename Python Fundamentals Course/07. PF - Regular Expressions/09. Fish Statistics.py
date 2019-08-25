import re

fish_pattern = r"(?P<tail>\>*)<{1}(?P<body>\(+)(?P<status>'|-|x){1}>{1}"
input_string = input()
fish_list = re.finditer(fish_pattern, input_string)
fish_len_check = list(fish_list)

if len(fish_len_check) > 0:
    for num, fish in enumerate(fish_len_check, 1):
        print(f"Fish {num}: {fish.group()}")
        if len(fish.group('tail')) == 0:
            print(f"  Tail type: None")
        elif len(fish.group('tail')) == 1:
            print(f"  Tail type: Short (2 cm)")
        elif len(fish.group('tail')) in range(2, 6):
            print(f"  Tail type: Medium ({len(fish.group('tail')) * 2} cm)")
        elif len(fish.group('tail')) > 5:
            print(f"  Tail type: Long ({len(fish.group('tail')) * 2} cm)")

        if len(fish.group('body')) <= 5:
            print(f"  Body type: Short ({len(fish.group('body')) * 2} cm)")
        elif len(fish.group('body')) in range(6, 11):
            print(f"  Body type: Medium ({len(fish.group('body')) * 2} cm)")
        elif len(fish.group('body')) > 10:
            print(f"  Body type: Long ({len(fish.group('body')) * 2} cm)")

        if fish.group('status') == "'":
            print("  Status: Awake")
        elif fish.group('status') == "-":
            print("  Status: Asleep")
        elif fish.group('status') == "x":
            print("  Status: Dead")
else:
    print("No fish found.")
