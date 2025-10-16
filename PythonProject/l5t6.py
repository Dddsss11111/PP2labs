import re

txt = input("Enter: ")

patt = r"[ ,.]"

result = re.sub(patt, ":", txt)

print("Result:", result)
