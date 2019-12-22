input_string = input()
input_list = input_string.split(" ")

data_dict = {}

while input_list[0] != "drop":
    if input_list[0] == "post" and input_list[1] not in data_dict.keys():
        data_dict[input_list[1]] = {"like": 0, "dislike": 0, "comment": {}}
    elif input_list[0] == 'like' or input_list[0] == 'dislike':
        if input_list[1] in data_dict.keys():
            data_dict[input_list[1]][input_list[0]] += 1
    elif input_list[0] == 'comment':
        if input_list[2] not in data_dict[input_list[1]]['comment'].keys():
            data_dict[input_list[1]]['comment'][input_list[2]] = []
            comment_string = input_string[(len(input_list[0] + " " + input_list[1] + " " + input_list[2]) + 1):]
            data_dict[input_list[1]]['comment'][input_list[2]].append(comment_string)
        else:
            comment_string = input_string[(len(input_list[0] + " " + input_list[1] + " " + input_list[2]) + 1):]
            data_dict[input_list[1]]['comment'][input_list[2]].append(comment_string)

    input_string = input()
    input_list = input_string.split(" ")

for post in data_dict.keys():
    print(f"Post: {post} | Likes: {data_dict[post]['like']} | Dislikes: {data_dict[post]['dislike']}")
    print("Comments:")
    if data_dict[post]['comment'] != {}:
        for k, v in data_dict[post]['comment'].items():
            for com in v:
                print(f"*  {k}: {com}")
    else:
        print("None")
