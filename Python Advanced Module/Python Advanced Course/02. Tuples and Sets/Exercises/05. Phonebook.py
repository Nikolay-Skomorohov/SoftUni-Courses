def function():
    result = {}
    while True:
        command = input().split("-")
        if command[0] == "search":
            break
        else:
            result[command[0]] = command[1]

    while True:
        to_search = input()
        if to_search == "stop":
            break
        elif to_search in result.keys():
            print(f"{to_search} -> {result[to_search]}")
        else:
            print(f"Contact {to_search} does not exist.")


function()
