import os
import shutil

r, d, files = next(os.walk('D:\\Testy'))
extensions = []
for f in files:
    file_ext = f.split('.')[-1]
    if file_ext not in extensions:
        extensions.append(file_ext)
    else:
        continue

for extension in extensions:
    os.mkdir(f'D:\\Testy\\{extension}')
    for file in files:
        if file.endswith(extension):
            shutil.move(f'D:\\Testy\\{file}', f'D:\\Testy\\{extension}\\')
