import re

txt = input("Enter a string: ")

result = re.split(r"(?=[A-Z])", txt)

print(result)
