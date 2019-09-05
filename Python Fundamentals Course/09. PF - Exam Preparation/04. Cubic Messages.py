import re


class Message:
    def __init__(self, text: str, length: int, before: str, after: str):
        self.text = text
        self.length = length
        self.before = before
        self.after = after
        self.code = None

    def calculate_code(self):
        verify_code = []
        for letter in self.before:
            try:
                verify_code.append(self.text[int(letter)])
            except:
                verify_code.append(" ")
        for char in self.after:
            try:
                verify_code.append(self.text[int(char)])
            except:
                verify_code.append(" ")

        self.code = "".join(verify_code)

    def __str__(self):
        return f"{self.text} == {self.code}"


def check_input(message: str, number_of_chars: int):
    pattern = r"(?P<before>[0-9]{1,})(?P<msg>[A-Za-z]{" + f"{number_of_chars}" + r"})(?P<after>[^A-Za-z]*)"
    if re.fullmatch(pattern, message):
        output = re.fullmatch(pattern, message)
        return Message(text=output.group('msg'),
                       length=number_of_chars,
                       before=output.group('before'),
                       after=output.group('after'))
    else:
        return None


def print_output(message_data: list):
    for item in message_data:
        item.calculate_code()
        print(item)


def main():
    message_data = []
    while True:
        message = input()
        number_of_chars = input()
        if message == "Over!":
            break
        else:
            number_of_chars = int(number_of_chars)
            message = check_input(message, number_of_chars)
            if message is not None:
                message_data.append(message)

    print_output(message_data)


if __name__ == '__main__':
    main()
