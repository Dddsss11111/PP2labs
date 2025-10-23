txt = input("Enter a string: ")

upper = sum(1 for c in txt if c.isupper())
lower = sum(1 for c in txt if c.islower())

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)