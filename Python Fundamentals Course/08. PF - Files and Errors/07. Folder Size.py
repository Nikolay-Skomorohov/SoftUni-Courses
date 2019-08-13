import os

root, dirs, files = next(os.walk('D:\\Testy\\'))

sizes = [os.stat(f"D:\\Testy\\{file}").st_size for file in files]
total_size = sum(sizes) / 1024 / 1024

with open('D:\\Testy\\output.txt', "w") as output_file:
    output_file.write(str(total_size))

