import re

txt = input("Enter: ")

patt = r"a.*b$"

if re.search(patt, txt):
    print("Match found!")
else:
    print("No match.")
