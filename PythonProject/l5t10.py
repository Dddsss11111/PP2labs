import re

txt = input("Enter a camelCase string: ")

snake = re.sub(r'([A-Z])', r'_\1', txt).lower()

print("snake_case:", snake)
