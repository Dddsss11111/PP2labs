import re

txt = input("Enter a string: ")

result = re.sub(r'([A-Z])', r' \1', txt)

print(result.strip())
