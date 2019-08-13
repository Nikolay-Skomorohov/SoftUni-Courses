with open('D:\\num1.txt', 'r') as first_file:
    with open('D:\\num2.txt', 'r') as second_file:
        with open('D:\\output.txt', 'w') as output_file:
            first_file_lines = first_file.readlines()
            second_file_lines = second_file.readlines()
            zipped = zip(first_file_lines, second_file_lines)
            for pair in zipped:
                output_file.write(pair[0].strip() + '\n')
                output_file.write(pair[1].strip() + '\n')

with open('D:\\output.txt', 'r') as output_file:
    print(output_file.read())
