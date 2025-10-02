# 1 Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

# class StrToUpper:
#     def __init__(self):
#         self.string = ""
#     def get_string(self):
#         self.string = input("Введите строку: ")
#     def printString(self):
#         print(self.string.upper())

# some_string = StrToUpper()
# some_string.get_string()
# some_string.printString()


# 2 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__(length)

#     def area(self):
#         print(self.length * self.length)

# sq = Square(3)
# sq.area()


# 3 Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# class Shape:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length, width)

#     def area(self):
#         print(self.length * self.width)

# rc = Rectangle(3, 4)
# rc.area()


# 4
# """
#     Write the definition of a Point class. Objects from this class should have a
#         a method show to display the coordinates of the point
#         a method move to change these coordinates
#         a method dist that computes the distance between 2 points
# """


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Coordinates of the point: ({self.x}, {self.y})")

#     def move(self):
#         x1, y1 = input("Input the coordinates of second point by the space: ").split(" ")
#         self.x = int(x1)
#         self.y = int(y1)
#         print(f"Point have been moved to new coordinates: ({self.x}, {self.y})")

#     def dist(self):
#         x1, y1 = input("Input the coordinates of second point by the space: ").split(" ")
#         c = ((self.x - int(x1))**2 + (self.y - int(y1)))**0.5
#         print(f"Distance between two points A({self.x}, {self.y}) and B({x1}, {y1}): d = {c}")

# point = Point(1, 2)
# point.show()
# point.move()
# point.dist()


# 5 reate a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# class Account:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0
#         print(f"Welcome {owner}. Your account balance: 0")

#     def deposit(self):
#         d = int(input(f"Your account balance: {self.balance}$. Enter the amount that you want to deposit: "))
#         self.balance += d
#         print(f"Succesfully. Your account balance: {self.balance}$")

#     def withdraw(self):
#         w = int(input(f"Your account balance: {self.balance}$. Enter the amount you want to withdraw: "))
#         if(w > self.balance):
#             print(f"you don't have that much money. Please, try again. Your account balance: ${self.balance}")
#             self.withdraw()
#         else:
#             self.balance -= w
#             print(f"Succesfully. Your account balance: {self.balance}$")


# Erasyl = Account("Erasyl Kokenov")
# Erasyl.deposit()
# Erasyl.withdraw()
# Erasyl.withdraw()


# 6 Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

# numbers = [i for i in range(2, 100)]
# prime_numbers = filter(lambda x : all(x % i != 0 for i in range(2, x)), numbers)
# result_list = list(prime_numbers)
# print(result_list)