import os
import string

folder_name = "letters"

os.makedirs(folder_name, exist_ok=True)

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    filepath = os.path.join(folder_name, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"This is file {filename}\n")

    print(f"Создан файл: {filepath}")

print("\n✅ Все файлы успешно созданы в папке:", folder_name)