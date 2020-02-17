class NameTooShortError(Exception):
    """ raise it when the name in the email is less than or equal to 4
    ("peter" will be the name in the email "peter@gmail.com" """
    pass


class MustContainAtSymbolError(Exception):
    """ Raise it when there is no "@" in the email """
    pass


class InvalidDomainError(Exception):
    """ Raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org) """
    pass


def email_validator(input_string: str):
    name = input_string.split("@")
    if len(name) == 1:
        raise MustContainAtSymbolError("Email must contain @")
    if len(name[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    if not input_string.endswith((".com", ".bg", ".org", ".net")):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    return "Email is valid"


def main():
    while 1:
        email_input = input()
        if email_input != "End":
            print(email_validator(email_input))
        else:
            break


if __name__ == "__main__":
    main()
