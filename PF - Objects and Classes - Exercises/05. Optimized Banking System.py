class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries


objects_list = []

input_list = input().split(" | ")

while input_list[0] != "end":
    if len(input_list) == 3:
        input_list[2] = "&".join(list(map(lambda x: "[" + x + "]", input_list[2].split(","))))
        web_object = Website(input_list[0], input_list[1], input_list[2])

    else:
        web_object = Website(input_list[0], input_list[1])
    objects_list.append(web_object)
    input_list = input().split(" | ")

for obj in objects_list:
    print(f"https://www.{obj.host}.{obj.domain}", end="")
    if obj.queries:
        print(f"/query?={obj.queries}")
    else:
        print("")
