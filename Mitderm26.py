# Bismillahir Rohmanir Rohim

# Recursion
# Less time
# Recursion calls itself directly or indirectly until the base problem is solved.

# def fuctorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fuctorial(n-1)    
# n = int(input("Enter a non-negative integer: "))
# if n <0:
#     print("Factorial is not defined for negative number: ")
# else:
#     result = fuctorial(n)
#     print("The factorial of " , n ,"is " , result )
  # ===========================================
    # ===========================================
    # ===========================================
# ===========================================
# Classes / Objects 

# class MyCalss: #  <== MyClass here is class name
    # x = 5 #  <==== 'X' here is property 
# print(MyCalss.x)

# ===========================================

# Creating an object 

# class MyCalss: #  <== MyClass here is class name
    # x = 1 #  <==== 'X' here is property 
# p1 =MyCalss()  < === object

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

# Object methods
# class Person:
#     def __init__(self,name,age): # <===== Constructor
#         self.name= name
#         self.age= age
#     def myperson(self):  #< === Method, the function inside a class
#         print("My name is " + self.name + ' and I am ' + self.age + ' years old')
# me = Person("Husan","17")
# me.age = "233"           # <=== modify object properties
# del me.age               # <=== delete object properties
# del me                   # <=== delete objects
# me.myperson()


# ===========================================

# The pass Statement
# class definitions cannot be empty, 
# but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

# class Person:
#     pass # <==== we typed here pass that is why there will be no errors

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== || 

# Inheritance
# Inheritance allows us to define a class that inherits another class’s methods and properties
# Parent class ===> Base class or Superclass
# Child class ===> Derived class (inherits from another class)

# A method = function inside a class   < ==== IMPORTANT!

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== || 

# class Person:  # Class (blueprint for objects)

#     def __init__(self, name, age):  # Constructor (runs when object is created) name and age are parameters
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

# class Person:  # Base class (parent class)

    # def __init__(self, fname, lname):  # Constructor (initializes object data)
        # self.Firstname = fname  # Instance variable (stores first name in object)
        # self.Lastname = lname   # Instance variable (stores last name in object)

    # def printname(self):  # Method (function inside class)
        # print(self.Firstname, self.Lastname)  # Accesses and prints object attributes


# class Student(Person):  # Derived class (child class) inheriting from Person
    # pass  # No new properties or methods; inherits everything from Person


# Creating an object of Student class
# x = Student("Ali", "Osl")  
# "Ali" → fname parameter, "Osl" → lname parameter
# Student uses Person's constructor (__init__) due to inheritance

# Calling inherited method
# x.printname()  
# Output: Ali Osl
# Method is defined in Person but used by Student object

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# class Person:  # Base class (parent class)

#     def __init__(self, fname, lname):  # Constructor (initializes object data)
#         self.Firstname = fname  # Instance variable (stores first name in object)
#         self.Lastname = lname   # Instance variable (stores last name in object)

#     def printname(self):  # Method (function inside class)
#         print(self.Firstname, self.Lastname)  # Accesses and prints object attributes


# class Student(Person):  # Derived class (child class) inheriting from Person
#     def __inti__(self,name,lastn):
#         Person.__inti__(self,name,lastn)

# # Creating an object of Student class
# x = Student("Ali", "Osl")  
# # "Ali" → fname parameter, "Osl" → lname parameter
# # Student uses Person's constructor (__init__) due to inheritance

# # Calling inherited method
# x.printname()  

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super(). __init__(fname, lname) # <=== It calls the constructor of the parent class (Person)
    
# x = Student("Mike", "Olsen")
# x.printname()

# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Add properties
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname,year):
#     super(). __init__(fname, lname) # <=== It calls the constructor of the parent class (Person)
#     self.graduateyear =year
    
# x = Student("Mike", "Olsen",'1122')
# x.printname()
# print(x.graduateyear)


# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||


# Iterators
# Lists, tuples, dictionaries, and sets are all iterable objects ==
# ===> All these objects have an iter() method for getting an iterator

# Iterable → something you can loop over (like a list)
# Iterator → the thing that goes through it step by step

# numbers = [10, 20, 30]

# it = iter(numbers)   # create iterator

# print(next(it))  # 10
# print(next(it))  # 20
# print(next(it))  # 30   

# Real-life example 🍎
# Imagine you have a box of apples.
# The box = a collection (list)
# Your hand taking apples one by one = an iterator
# You don’t grab all apples at once.
# You take:
# first apple
# then next
# then next
# …until there are no apples left
# 👉 That “taking one by one” process = iteration
# 👉 The thing that helps you do it = iterator


# Example

# mytuple = ("Apple","banana","cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# numbers = (1,2,4,5,6)
# number = iter(numbers)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/     / ||
#                                                                  /  ||
#                                                                  /  ||
#                                                                  /  ||
#                                                                  /  ||
# Even strings are iterable objects and can return an iterator.<===   ||
#                                                                  \  ||
#                                                                  \  ||
#                                                                  \  ||
#                                                                  \  ||
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/     \ ||


# Strings are also iterable objects, containing a sequence of characters. ==>
# mystr= "banana"
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||


# Polymorphism
# The word "polymorphism" means "many forms” in programming;
# it refers to methods/functions/operators with the same name that can be executed on 
# many objects or classes.

# An example of a Python function that can be used on different objects is the len() function.

# For strings, len() returns the number of characters; for tuples,===>
# ===> len() returns the number of items in the tuple; for dictionaries,===>
# ==> len() returns the number of key/value pairs in the dictionary.

# Polymorphism is often used in class methods, where multiple classes can have the same method name.


# ====================================================== ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Global Keyword
# The global keyword makes the variable global

# The variable belongs to the global scope if you use the global keyword.

# x =200
# def myfunc():
    # global x
    # x = 300   #<=== local variable
# myfunc() # < === calling the local variable
# print(x)
# use the global keyword if you want to make a change to a global variable inside a function.


# ====================================================== ||
# ////////////////////////////////////////////////////// ||

# Polymorphism
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       # Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") # Create a Boat object
# plane1 = Plane("Boeing", "747")     # Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()


# ====================================================== ||
# ////////////////////////////////////////////////////// ||

# Inheritance Class Polymorphism
# idk !!


# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Scope
# A variable is only available from inside the region it is created. This is called scope


# Local Scope
# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.

# A variable created inside a function is available inside that function.
# def myfunc():
#   x = 300
#   print(x)
# myfunc()

# =====================================================  ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Function Inside Function
# The local variable can be accessed from a function within the function.

# def myfunc():
    # x = 300  
    # create a variable x inside this function

    # def myinnerfunc():
        # this is a function inside another function

        # print(x)
        # print x (it takes x from the outer function)

    # myinnerfunc()
    # run the inner function

# myfunc()
# run the main function

# Key idea here
# 👉 The inner function can access variables from the outer function

# Practice 
# def main():
#     x =12
#     def derived():
#         print(x)
#     derived()
# main()

# =====================================================  ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Global scope
# A variable created in the main body of the Python code is a global variable ,
# and belongs to the global scope.

# Global variables are available from within any scope, global and local.

# A variable created outside of a function is global and can be used by anyone.

# x = 200
# global variable (everyone can use it)

# def myf():
    # print(x)
    # uses x from outside (global)

# myf()
# calls the function → prints x

# print(x)
# prints x again from global scope

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# x = 200
# def myf():
    # x = 100  # new local variable, not global
# myf()
# print(x)  
# Output : still 200

# =======================================================================

# x = 200

# def myf():
    # global x #<====
    # x = 100

# myf()
# print(x)  
#   Output : 100
    
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
    
# Naming Variables

# If you operate with the same variable name inside and outside of a function,

# Python will treat them as two separate variables, one available in the global scope ===>
# (outside the function) and one available in the local scope (inside the function).

# Ex: The function will print the local x, and then the code will print the global x.
# x = 300
# def myfunc():
#   x = 200
#   print(x)
# myfunc()
# print(x)
# Output: 200
#         300

# =====================================================  ||
# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Modules 
# Module = just another Python file
# ________________________________________________________
#|Real-life analogy                                       |
#|                                                        |      
#|Think like this:                                        |
#|Your main program = your room                           |
#|Module = another room with tools                        |
#|Instead of rewriting tools, you just go and usethem     |
#|________________________________________________________|

# main.py  ──────► mymodule.py
#    │                │
#    │ calls          │ has function
#    ▼                ▼
#  greeting()     def greeting()


# from modules import a as A  # <== importing module form another file
# print(A) # <== printing A from another module

# =====================================================  ||
# ////////////////////////////////////////////////////// ||

# Built-in Modules
# Import and use the platform module.

# import platform
# x = platform.system()
# print(x)
# //////////////////////////////////////
# Dir function
# There is a  dir() built-in function to list all the function names
# (or variable names) in a module. 

# import platform
# x =dir(platform)
# print(x)

# /////////////////////////////////////

# Import From Module
# You can choose to import only parts from a module, by using the from keyword
from modules import person1
print (person1["country"])

# do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]

# ////////////////////////////////////////////////////// ||
# ====================================================== ||
