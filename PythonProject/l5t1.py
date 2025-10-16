import re

pattern = r'ab*'

test_strings = ["a", "ab", "abb", "b", "ac", "aab"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"{s} → Match")
    else:
        print(f"{s} → No match")
