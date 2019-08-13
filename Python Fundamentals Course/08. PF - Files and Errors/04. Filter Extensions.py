import os

for r, d, f in os.walk('D:\\Testy'):
    for file in f:
        if file.endswith('.txt'):
            print(file)
