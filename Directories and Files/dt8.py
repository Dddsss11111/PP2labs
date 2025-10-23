import os

path = input("Введите путь к файлу, который нужно удалить: ")

if os.path.exists(path):

    if os.path.isfile(path):

        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print(f"\nФайл '{path}' успешно удалён.")
            except Exception as e:
                print("\nОшибка при удалении файла:", e)
        else:
            print("\nНет прав на удаление этого файла.")
    else:
        print("\nУказанный путь существует, но это не файл.")
else:
    print("\nУказанный путь не существует.")