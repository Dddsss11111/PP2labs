import time
import math

num = int(input("Enter a number: "))
milliseconds = int(input("Enter a miliseconds: "))

time.sleep(milliseconds/1000)

result = math.sqrt(num)

print(f"Square root of {num} after {milliseconds} milliseconds is {result}")