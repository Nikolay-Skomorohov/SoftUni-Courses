input_list = list(input().split(' -> '))

data_dict = {}

while input_list[0] != "login":
    data_dict[input_list[0]] = input_list[1]
    input_list = list(input().split(' -> '))

login_list = list(input().split(' -> '))
counter = 0
while login_list[0] != 'end':
    if login_list[0] in data_dict.keys() \
                    and login_list[1] == data_dict[login_list[0]]:
        print(f"{login_list[0]}: logged in successfully")

    else:
        counter += 1
        print(f"{login_list[0]}: login failed")

    login_list = list(input().split(' -> '))

print(f"unsuccessful login attempts: {counter}")
