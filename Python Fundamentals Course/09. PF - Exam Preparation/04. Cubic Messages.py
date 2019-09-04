import re


class Message:
    def __init__(self, text: str, length: int, before: str, after: str):
        self.text = text
        self.length = length
        self.before = before
        self.after = after
        self.code = None

    def calculate_code(self):

        return

    def __str__(self):
        return f"{self.text}=={self.code}"


def check_input(message: str, number_of_chars: int):
    pattern = r"(?P<before>[0-9]{1,})(?P<msg>[A-Za-z]{" + f"{number_of_chars}" + r"})(?P<after>[^A-Za-z]{1,})"
    if re.match(pattern, message):
        output = re.match(pattern, message)
        return Message(text=output.group('msg'),
                       length=number_of_chars,
                       before=output.group('before'),
                       after=output.group('after'))
    else:
        return None


def print_output(message_data: list):
    for item in message_data:
        item.calulate_code()
        print(item)


def main():
    message_data = []
    while True:
        message = input()
        number_of_chars = int(input())
        if message == "Over!":
            break
        else:
            message = check_input(message, number_of_chars)
            if message:
                message_data.append(message)

    print_output(message_data)


if __name__ == '__main__':
    main()
