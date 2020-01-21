input_text = input()
char_list = list(input_text)
open_list = []

for i in range(len(char_list)):
    if char_list[i] in "({[":
        open_list.append(char_list[i])
    elif open_list:
        if char_list[i] == ")" and open_list[-1] == "(":
            open_list.pop()
        elif char_list[i] == "}" and open_list[-1] == "{":
            open_list.pop()
        elif char_list[i] == "]" and open_list[-1] == "[":
            open_list.pop()
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()

if open_list:
    print("NO")
else:
    print("YES")
