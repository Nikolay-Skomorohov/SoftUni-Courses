while True:
    input_list = input()
    if input_list != "stop playing":
        input_numbers = [int(x) for x in input_list.split()]
        if list(sorted(set(input_numbers))) == sorted(input_numbers):
            unique_list = []
            for element in input_numbers:
                if element % 2 == 1:
                    unique_list.append(element)
                elif element % 2 == 0:
                    unique_list.append(element + 2)
            unique_list.sort()
            unique_str = list(map(str, unique_list))
            print(f"Unique list: {','.join(unique_str)}")
            print(f"Output: {sum(unique_list) / len(unique_list):.2f}")

        else:
            non_unique_list = []
            for element in input_numbers:
                if element % 2 == 1:
                    non_unique_list.append(element + 3)
                elif element % 2 == 0:
                    non_unique_list.append(element)
            non_unique_list.sort()
            non_unique_str = list(map(str, non_unique_list))
            print(f"Non-unique list: {':'.join(non_unique_str)}")
            print(f"Output: {sum(non_unique_list) / len(non_unique_list):.2f}")
    else:
        break
