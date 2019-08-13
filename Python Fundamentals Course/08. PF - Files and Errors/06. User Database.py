current_login_user = None
user_database_text = {}
while True:
    input_command = input().split()

    if input_command[0] == 'register':
        if input_command[1] in user_database_text.keys():
            print('The given username already exists.')
            continue
        else:
            if not input_command[2] == input_command[3]:
                print('The two passwords must match.')
                continue
            else:
                user_database_text[input_command[1]] = input_command[2]

    elif input_command[0] == 'login':
        if current_login_user is not None:
            print('The given username already exists.')
            continue
        elif input_command[1] not in user_database_text.keys():
            print('There is no user with the given username.')
            continue
        elif input_command[1] in user_database_text.keys():
            if input_command[2] != user_database_text[input_command[1]]:
                print('The password you entered is incorrect.')
                continue
            else:
                current_login_user = input_command[1]

    elif input_command[0] == 'logout':
        if current_login_user is None:
            print('There is no currently logged in user.')
            continue
        else:
            current_login_user = None

    elif input_command[0] == 'exit':
        with open('D:\\Testy\\users.txt', 'w') as output_file:
            for values in user_database_text.keys():
                output_file.write(str(values))
