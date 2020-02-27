class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


emails_list = []
while 1:
    command = input().split(" ")
    if command[0] == "Stop":
        break
    else:
        emails_list.append(Email(*command))


sent_list = list(map(int, input().split(", ")))
for mail in range(len(emails_list)):
    if mail in sent_list:
        emails_list[mail].send()
    print(emails_list[mail].get_info())
