with open('D:\\input.txt', 'r') as input_text:
    with open('D:\\output.txt', 'w') as output_text:
        for line, text in enumerate(input_text.readlines(), 1):
            output_text.write(f"{line}. {text}")

with open('D:\\output.txt', 'r') as print_text:
    print(print_text.read())
