import psycopg2
import csv

DB_SETTINGS = {
    "host": "localhost",
    "port": 5432,
    "dbname": "lab10",
    "user": "postgres",
    "password": "Gitler1939",
    "client_encoding": "UTF8"
}

try:
    connection = psycopg2.connect(
        host=DB_SETTINGS["host"],
        port=DB_SETTINGS["port"],
        dbname=DB_SETTINGS["dbname"],
        user=DB_SETTINGS["user"],
        password=DB_SETTINGS["password"],
    )
    connection.set_client_encoding(DB_SETTINGS["client_encoding"])
except Exception as conn_error:
    print("Не удалось подключиться к базе данных:", conn_error)
    exit(1)

cursor = connection.cursor()
first_launch = True

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    user_phone VARCHAR(255)
);
""")
connection.commit()

while True:

    if first_launch:
        first_launch = False
        print(
            "Добро пожаловать в телефонный справочник!\n"
            "Здесь вы можете сохранять контакты:\n"
            "- Имя\n"
            "- Телефонный номер\n\n"
            "Данные можно внести вручную или импортировать из CSV.\n"
        )

    print(
        "Меню действий:\n"
        "1 — Добавить запись вручную\n"
        "2 — Загрузить записи из CSV файла\n"
        "3 — Изменить номер по имени\n"
        "4 — Изменить имя по номеру\n"
        "5 — Показать имена, начинающиеся на букву\n"
        "6 — Удалить запись по телефону\n"
        "7 — Завершить работу\n"
    )

    try:
        choice = int(input("Выберите пункт: "))
    except ValueError:
        print("Пожалуйста, введите номер пункта!\n")
        continue

    if choice == 1:
        name_input = input("Введите имя: ").strip()
        phone_input = input("Введите телефон: ").strip()

        try:
            cursor.execute(
                "INSERT INTO users (username, user_phone) VALUES (%s, %s)",
                (name_input, phone_input)
            )
            connection.commit()
            print("Контакт добавлен!\n")
        except Exception as insert_err:
            print("Ошибка при добавлении:", insert_err, "\n")

    elif choice == 2:
        file_path = input("Укажите путь к CSV: ").strip()

        try:
            with open(file_path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)

                counter = 0
                for line in reader:
                    if len(line) < 3:
                        continue
                    try:
                        cursor.execute(
                            "INSERT INTO users (username, user_phone) VALUES (%s, %s)",
                            (line[1], line[2])
                        )
                        counter += 1
                    except Exception as line_err:
                        print("Строка пропущена:", line, "| Причина:", line_err)

                connection.commit()
                print(f"Импорт завершён. Добавлено записей: {counter}\n")

        except FileNotFoundError:
            print("Файл не найден!\n")
        except Exception as csv_err:
            print("Ошибка при обработке CSV:", csv_err, "\n")

    elif choice == 3:
        old_name = input("Укажите имя: ").strip()
        new_phone = input("Введите новый номер: ").strip()

        cursor.execute(
            "UPDATE users SET user_phone = %s WHERE username = %s",
            (new_phone, old_name)
        )
        connection.commit()
        print("Обновление выполнено! Изменено:", cursor.rowcount, "\n")

    elif choice == 4:
        old_phone = input("Введите номер: ").strip()
        updated_name = input("Новое имя: ").strip()

        cursor.execute(
            "UPDATE users SET username = %s WHERE user_phone = %s",
            (updated_name, old_phone)
        )
        connection.commit()
        print("Имя успешно изменено! Изменено:", cursor.rowcount, "\n")

    elif choice == 5:
        symbol = input("Введите начальную букву: ").strip()
        cursor.execute(
            "SELECT username, user_phone FROM users WHERE username ILIKE %s",
            (symbol + "%",)
        )
        data = cursor.fetchall()

        if data:
            for entry in data:
                print(entry[0], "-", entry[1])
        else:
            print("Совпадений нет.")
        print()

    elif choice == 6:
        del_phone = input("Введите номер для удаления: ").strip()

        cursor.execute(
            "DELETE FROM users WHERE user_phone = %s",
            (del_phone,)
        )
        connection.commit()
        print("Удалено записей:", cursor.rowcount, "\n")

    elif choice == 7:
        print("Программа завершена.")
        break

    else:
        print("Такого пункта нет!\n")

cursor.close()
connection.close()
