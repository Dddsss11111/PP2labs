import re

txt = input("Enter: ")

patt = r"[A-Z][a-z]+"

match = re.findall(patt, txt)

print("Match found:", match)
