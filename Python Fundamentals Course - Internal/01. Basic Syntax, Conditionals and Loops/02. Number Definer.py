input_number = float(input())

if input_number == 0:
    print("zero")
elif input_number > 0:
    if input_number < 1:
        print("small positive")
    elif abs(input_number) > 1000000:
        print("large positive")
    else:
        print("positive")
elif input_number < 0:
    if abs(input_number) < 1:
        print("small negative")
    elif abs(input_number) > 1000000:
        print("large negative")
    else:
        print("negative")
