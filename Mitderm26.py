# Bismillahir Rohmanir Rohim

# Recursion
# Less time
# Recursion calls itself directly or inderectly until the base problem is solved.

# def fuctorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fuctorial(n-1)    
# n = int(input("Enter a non-negative integer: "))
# if n <0:
#     print("FActorial is not defined for negative number: ")
# else:
#     result = fuctorial(n)
#     print("The factorial of " , n ,"is " , result )
  # ===========================================
    # ===========================================
    # ===========================================
# ===========================================
# Classes /Objects 

# class MyCalss: #  <== MyClass here is class name
    # x = 5 #  <==== 'X' here is property 
# print(MyCalss.x)

# ===========================================

# Creating an object 

# class MyCalss: #  <== MyClass here is class name
    # x = 1 #  <==== 'X' here is property 
# p1 =MyCalss() 

# print(p1.x)
# ===========================================

# __init__() function
# class human:
#     def __init__(self,name,age):
#         self.name= name # <==== self tells Python: "Store this data on THIS specific object"
#         self.age= age   # <==== self tells Python: "Store this data on THIS specific object"
# Person_one = human("Ali","19")
# Person_two = human("Behruz","16")
# print("His name is ",Person_one.name," and he is ",Person_one.age ,"years old")
# print("His name is ",Person_two.name," and he is ",Person_two.age ,"years old")

# ===========================================

# Opject methods
# class Person:
#     def __init__(self,name,age): # <===== Costructor
#         self.name= name
#         self.age= age
#     def myperson(self):
#         print("My name is " + self.name + ' and i am ' + self.age + ' years old')
# me = Person("Husan","17")
# me.age = "233"           # <=== modefy object properties
# del me.age               # <=== delete object properties
# del me                   # <=== delete objects
# me.myperson()


# ===========================================

# The pass Statement
# class definitions cannot be empty, 
# but if you for some reason have a class definition with no content, 
# put it in the pass statement to avoid getting an error.

# class Person:
#     pass # <==== we typed here pass that is why there will be no errors

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== || 
# Inheretance
# Inheritance allows us to define a class that inherits another class’s methods and properties
# Parent class ===> Base-class or Superclass
# Child class ===> Derived-class (Inherets from another class)

# A method = function inside a class   < ==== IMOORTANT!

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== || 

# class Person:  # Class (blueprint for objects)

#     def __init__(self, name, age):  # Constructor (runs when object is created) name and age is parameter
#         self.name = name  # Instance variable (stored in object)
#         self.age = age    # Instance variable

#     def My_student(self):  # Method (function inside class)
#         print("My student is", self.name, "and he is", self.age, "years old")

# # Creating an object (instance of the class)
# st1 = Person("Muslim", "16")

# # Calling a method using the object
# st1.My_student()

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

class Person:  # Base class (parent class)

    def __init__(self, fname, lname):  # Constructor (initializes object data)
        self.Firstname = fname  # Instance variable (stores first name in object)
        self.Lastname = lname   # Instance variable (stores last name in object)

    def printname(self):  # Method (function inside class)
        print(self.Firstname, self.Lastname)  # Accesses and prints object attributes


class Student(Person):  # Derived class (child class) inheriting from Person
    pass  # No new properties or methods; inherits everything from Person


# Creating an object of Student class
x = Student("Ali", "Osl")  
# "Ali" → fname parameter, "Osl" → lname parameter
# Student uses Person's constructor (__init__) due to inheritance

# Calling inherited method
x.printname()  
# Output: Ali Osl
# Method is defined in Person but used by Student object