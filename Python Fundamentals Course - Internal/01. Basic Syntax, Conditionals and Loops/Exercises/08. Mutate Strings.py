first_string = input()
second_string = input()

temp_string = first_string

if first_string != second_string:
    for index in range(len(first_string)):
        for char in first_string[index]:
            if char != second_string[index]:
                temp_string = temp_string[:index] + second_string[index] + temp_string[index + 1:]
                print(temp_string)
                break

