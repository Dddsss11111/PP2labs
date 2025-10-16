import re

txt = input("Enter: ")

patt = r"[a-z]+_[a-z]+"

match = re.findall(patt, txt)

print("Match found:", match)
