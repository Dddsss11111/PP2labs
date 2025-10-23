filename = input("Enter name of file or path: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print("Number of lines in file:", len(lines))
except FileNotFoundError:
    print("The specified file was not found.")

# C:\Users\Madina Zheleu\OneDrive\Рабочий стол\lab\LAB1\LAB6\Python Directories and Files exercises\sample.txt