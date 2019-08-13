with open('D:\\input.txt', 'r') as input_file:
    with open('D:\\output.txt', 'w') as output_file:
        for line, text in enumerate(input_file):
            if line % 2 == 1:
                output_file.write(text)
            else:
                pass

with open('D:\\output.txt', 'r') as text_file:
    print(text_file.read())
