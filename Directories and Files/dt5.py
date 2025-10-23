
import os

my_list = ['apple', 'banana', 'cherry', 'orange']
filename = 'fruits.txt'

with open(filename, 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item + '\n')

print("Список успешно записан в файл:", filename)