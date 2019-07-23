class User:
    def __init__(self, username: str,
                 received_messages = []):
        self.username = username
        self.received_messages = received_messages


class Message:
    def __init__(self, content: str, sender: str):
        self.content = content
        self.sender = sender


def create_user(name):
    return User(name)


def add_message(to_user: User, message: Message):
    to_user.received_messages.append(message)


def create_message(sender, message):
    return Message(message, sender)


def print_history(user1, user2):
    print(user1, user2)
    for message in User(user1).received_messages:
        print(f"{user1}: {message}")


def main():
    input_list = [item for item in input().split()]

    user_list = []

    while input_list[0] != "exit":
        if input_list[0] == "register":
            new_user = create_user(input_list[1])
            user_list.append(new_user)
        elif len(input_list) > 2 and input_list[2] == "send":
            if input_list[0] in user_list and input_list[2] in user_list:
                new_message = create_message(input_list[0], input_list[3])
                add_message(), new_message)

        input_list = [item for item in input().split()]

    users_history = [user for user in input().split()]
    print_history(users_history[0], users_history[1])

if __name__ == "__main__":
    main()