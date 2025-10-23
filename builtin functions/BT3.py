import string

txt = input("Enter a string: ")

cleaned = ''.join(c.lower() for c in txt if c.isalnum())

if cleaned == cleaned[::-1]:
    print(f"Строка '{txt}' является палиндромом.")
else:
    print(f"Строка '{txt}' не является палиндромом.")