source_file = input("Введите имя исходного файла: ")
destination_file = input("Введите имя файла, в который нужно скопировать: ")

try:

    with open(source_file, 'r', encoding='utf-8') as src:

        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())

    print(f"\nСодержимое успешно скопировано из '{source_file}' в '{destination_file}'.")

except FileNotFoundError:
    print("\nИсходный файл не найден. Проверьте путь и попробуйте снова.")