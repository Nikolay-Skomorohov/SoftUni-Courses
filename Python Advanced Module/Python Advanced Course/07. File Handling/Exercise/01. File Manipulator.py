import re
from os import remove


def create_file(filename: str):
    open(filename, "w")


def add_to_file(filename: str, new_string: str):
    new_content = new_string
    file = open(filename, "a")
    file.write(new_content + "\n")
    file.close()


def replace_string(filename: str, old_string: str, new_string: str):
    try:
        file = open(filename, "r")
        reg_ex_string = re.sub(old_string, new_string, file.read())
        file.close()
        file = open(filename, "w")
        file.write(reg_ex_string)
        file.close()
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename: str):
    try:
        remove(filename)
    except FileNotFoundError:
        print("An error occurred")


def file_manipulator(command: str):
    command = command.split("-")
    filename = command[1]
    if command[0] == "Create":
        create_file(filename)
    elif command[0] == "Add":
        add_to_file(filename, command[2])
    elif command[0] == "Replace":
        replace_string(filename, command[2], command[3])
    elif command[0] == "Delete":
        delete_file(filename)


def main():
    while 1:
        command = input()
        if command == "End":
            break
        else:
            file_manipulator(command)


if __name__ == "__main__":
    main()
