def check_pass(password: str):
    valid = True
    if not password.isalnum():
        valid = False
        print("Password must consist only of letters and digits")

    if not len(password) in range(6, 11):
        valid = False
        print("Password must be between 6 and 10 characters")

    count = 0
    for char in password:
        if char.isdigit():
            count += 1

    if count < 2:
        valid = False
        print("Password must have at least 2 digits")

    if valid is True:
        print("Password is valid")


pass_input = input()
check_pass(pass_input)
