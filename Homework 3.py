#Задание3

file_names = ['1.txt', '2.txt', '3.txt']
file_info = []

for file_name in file_names:
    with open(file_name, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))

file_info.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='UTF-8') as f:
    for file_name, line_count, lines in file_info:
        counting = 0
        for line in lines:
            f.write(f'Cтрока номер {counting} файла номер {file_name} : {line.strip()}\n')
            counting += 1
