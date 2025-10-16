import re

txt = input("Enter: ")

patt = r"ab{2,3}"

if re.search(patt, txt):
    print("Match found!")
else:
    print("No match.")
