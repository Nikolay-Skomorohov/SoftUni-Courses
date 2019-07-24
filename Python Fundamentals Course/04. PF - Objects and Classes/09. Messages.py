import itertools


class User:
    def __init__(self, username: str):
        self.username = username
        self.received_messages = []


class Message:
    def __init__(self, content: str, sender: User):
        self.content = content
        self.sender = sender


def create_user(name):
    return User(name)


def add_message(to_user: User, message: Message):
    to_user.received_messages.append(message)


def create_message(sender: User, message):
    return Message(message, sender)


def check_users_for_messages(user1: User, user2: User):
    user1_to_user2 = []
    user2_to_user1 = []
    for message_user in user1.received_messages:
        if message_user.sender == user2:
            user2_to_user1.append(message_user)

    for message_user in user2.received_messages:
        if message_user.sender == user1:
            user1_to_user2.append(message_user)
    result = (user1_to_user2, user2_to_user1)
    return result


def print_history(user1, user2):
    info = check_users_for_messages(user1, user2)
    if info[0] == [] and info[1] == []:
        print("No messages")
    else:
        for message, message2 in itertools.zip_longest(user2.received_messages, user1.received_messages):
            if message and message.sender == user1:
                print(f"{user1.username}: {message.content}")
            if message2 and message2.sender == user2:
                print(f"{message2.content} :{user2.username}")


def main():
    user_list = []
    input_list = [item for item in input().split()]
    while input_list[0] != "exit":
        if input_list[0] == "register":
            new_user = create_user(input_list[1])
            user_list.append(new_user)
        elif len(input_list) > 2 and input_list[1] == "send":
            if input_list[2] in [user.username for user in user_list]\
                    and input_list[0] in [user.username for user in user_list]:
                sender = next(user for user in user_list if user.username == input_list[0])
                receiver = next(user for user in user_list if user.username == input_list[2])
                new_message = create_message(sender, input_list[3])
                add_message(receiver, new_message)

        input_list = [item for item in input().split()]

    users_history = [user for user in input().split()]
    first_user = next(user for user in user_list if user.username == users_history[0])
    second_user = next(user for user in user_list if user.username == users_history[1])
    print_history(first_user, second_user)


if __name__ == "__main__":
    main()
