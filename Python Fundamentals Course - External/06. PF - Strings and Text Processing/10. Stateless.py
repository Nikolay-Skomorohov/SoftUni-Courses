input_state = input()
input_fiction = input()

result = []
while True:
    input_state = input_state.replace(input_fiction, "")
    while len(input_fiction) > 2:
        input_fiction = input_fiction[1:-1]
        input_state = input_state.replace(input_fiction, "")
    input_fiction = input_fiction[1:-1]
    input_state = input_state.replace(input_fiction, "")
    result.append(input_state)

    input_state = input()
    if input_state == 'collapse':
        break
    else:
        input_fiction = input()


for whatever in result:
    if whatever != '':
        print(whatever)
    else:
        print("(void)")

