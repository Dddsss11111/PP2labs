# 1
# class Student(Person):


# 2
# class Person:
#   def __init__(self, fname):
#     self.firstname = fname

#   def printname(self):
#     print(self.firstname)

# class Student(Person):
#   pass

# x = Student("Mike")
# x.printname()






# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)



# Examples

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)