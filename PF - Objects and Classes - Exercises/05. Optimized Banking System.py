class Bank_account:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


objects_list = []

input_list = input().split(" | ")

while input_list[0] != "end":
    bank_object = Bank_account(name=input_list[1],
                               bank=input_list[0],
                               balance=float(input_list[2]))
    objects_list.append(bank_object)
    input_list = input().split(" | ")

sorted_result = sorted(objects_list, key=lambda x: (-x.balance,
                                                    len(x.bank)))

for obj in sorted_result:
    print(f"{obj.name} -> {obj.balance:.2f} ({obj.bank})")
