import re

txt = input("Enter a snake_case string: ")

parts = txt.split('_')

camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])

print("CamelCase:", camel_case)
