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
    # def __init__(self,name,age): # <===== Constructor
        # self.name= name
        # self.age= age
    # def myperson(self):  #< === Method, the function inside a class
        # print("My name is " + self.name + ' and I am ' + self.age + ' years old')
# me = Person("Husan","17")
# me.age = "233"           # <=== modify object properties
# del me.age               # <=== delete object properties
# del me                   # <=== delete objects
# me.name  ="Ali"

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

    # def __init__(self, fname, lname):  # Constructor (initializes object data)
        # self.Firstname = fname  # Instance variable (stores first name in object)
        # self.Lastname = lname   # Instance variable (stores last name in object)

    # def printname(self):  # Method (function inside class)
        # print(self.Firstname, self.Lastname)  # Accesses and prints object attributes


# class Student(Person):  # Derived class (child class) inheriting from Person
    # def __inti__(self,name,lastn):
        # Person.__inti__(self,name,lastn)

# Creating an object of Student class
# x = Student("Ali", "Osl")  
# "Ali" → fname parameter, "Osl" → lname parameter
# Student uses Person's constructor (__init__) due to inheritance

# Calling inherited method
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
# 👉 super() means:
# “Go to parent class and use its methods”
    
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
# a = "Iterable"
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

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
#     global x
#     x = 300   #<=== local variable
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

# def main():
#     x=  999
#     def mini():
#         print(x)
#     mini()
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

# ============================BUT===========================================>

# x = 200

# def myf():
#     global x #<====
#     x = 100

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

# ====================================================== ||
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
#|Instead of rewriting tools, you just go and use them    |
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
# from modules import person1
# print (person1["country"])

# do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]


# ////////////////////////////////////////////////////// ||
# ====================================================== ||

# Datetime

from datetime import datetime
# x = datetime.datetime.now()
# print(x)
# Output like : 2026-03-23 00:42:20.304694

# The date contains Year, Month, Day, Hour, Minute, Second, and Microsecond.


# Ex: Return the year and name of weekday
# x = datetime.now()
# print("This year is ", x.strftime("%Y ") ," and ", " the weekday is " , x.strftime("%A"))


# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
# %A = full day name
# strftime )==> means ====>“format date/time into a string”

# x = datetime.now()
# print(x.day)
# print(x.strftime("%A"))


# Visual idea ==>
# x = 2026-03-23

# x.year      → 2026
# x.strftime  → "Monday"


# ////////////////////////
# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
# import datetime
# x= datetime(2020,5,15)
# print(x)

# ///////////////////////////////

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, ===>
# format, to specify the format of the returned string

# ///////////////////////////

# =============================
# >>>  Datetime (countunue) <<<
# =============================

# Display the name of the month.

# import datetime
# z = datetime.datetime(2018,6,1)
# print(z.strftime("%B")) # <===%B shows Month

# print("=============")
# %a - Weekday, short version
# w = datetime.datetime.now()
# print(w.strftime("%a"))

# print("=============")
# %A-Weekday, full version

# W = datetime.datetime.now()
# print(W.strftime("%A"))

# print("=============")

# %w-Weekday as a number 0-6, 0 is Sunday

# x = datetime.datetime.now()
# print(x.strftime("%w"))

# print("=============")

# %d-Day of month 01-31

# x = datetime.datetime.now()
# print(x.strftime("%d"))

# print("=============")
# %b-Month name, short version

# x = datetime.datetime.now()
# print(x.strftime("%b"))

# print("=============")

# %B-Month name, full version
# x = datetime.datetime.now()
# print(x.strftime("%B"))

# print("=============")

# %m-Month as a number 01-12
# x = datetime.datetime.now()
# print(x.strftime("%m"))

# print("=============")

# %y-Year, short version, without century

# x = datetime.datetime.now()
# print(x.strftime("%y"))

# print("=============")

# %Y-Year, full version
# x = datetime.datetime.now()
# print(x.strftime("%Y"))

# print("=============")

# %H-Hour 00-23

# x = datetime.datetime.now()
# print(x.strftime("%H"))

# print("=============")
# %I-Hour 00-12
# x = datetime.datetime.now()
# print(x.strftime("%I"))

# print("=============")
# %p-AM/PM


# //////////////////////////////
# x = datetime.datetime.now()
# print(x.strftime("%H") + x.strftime("%p"))
# /////////////////////////////

# print("=============")
# %M-Minute 00-59
# x = datetime.datetime.now()
# print(x.strftime("%M"))

# print("=============")
    # %S-Second 00-59
# x = datetime.datetime.now()
# print(x.strftime("%S"))


# print("=============")
    # %j-Day number of year 001-366
# x = datetime.datetime.now()
# print(x.strftime("%j"))



#1 %A-Weekday, full version ✅
#2 %a - Weekday, short version ✅
#3 %B-Month name, full version ✅
#4 %b-Month name, short version ✅
#5 %d-Day of month 01-31 ✅
#6 %M-Minute 00-59 ✅
#7 %m-Month as a number 01-12✅
#8 %Y-Year, full version ✅
#9 %y-Year, short version, without century ✅
#10 %w-Weekday as a number 0-6, 0 is Sunday ✅
#11 %H-Hour 00-23 ✅
#12 %I-Hour 00-12 ✅
#13 %p-AM/PM ✅
#14 %S-Second 00-59 ✅
#15 %j-Day number of year 001-366 ✅

# mo = datetime.datetime.now()
# print("Today is " , mo.strftime("%A"), " and this year is " +mo.strftime("%Y"), "so today is " + mo.strftime("%j"), "'s day of a year", "and the time is " + mo.strftime("%H"))

# ====================================================== ||
# //////////////////////>>>  MATH <<<<////////////////// ||
# ====================================================== ||


# min() and max()  <==> functions can be used to find the lowest or highest value in an iterable.

# x = min(13,4,65,2,45654,7,6,54,2345)  # <<==================
# y = max(56543,654,3,45,2,45,0.4,76,3,4)   # <<==================
# print(x)
# print(y)
# ////////////////////////////////////////////////////////////////////////////////////////

# The abs() function returns the specified number's absolute (positive) value.
# x = abs(-10000)  # <<==================
# print(x)

# ////////////////////////////////////////////////////////////////////////////////////////


# The pow(x, y) function returns the value of x to the power of y (x^y).

# Return the value of 4 to the power of 3 (same as 4 * 4 * 4)
# x = pow(2,3) # <<==================
# print(x)

# ////////////////////////////////////////////////////////////////////////////////////////

# The Math Module
import math

# The math.sqrt() method returns the square root of a number.
# x = math.sqrt(64) # <<==================
# print(x) 

# x= math.sqrt(49)
# print(x)

# ..............................................................................

#Round a number upward to its nearest integer  # <<==================
# x = math.ceil(1.4) 
# x= math.ceil(1.1)
#Round a number downward to its nearest integer # <<==================
# y = math.floor(1.9)
# print(x)
# print(y)



# //////////////////////////////

# The math.pi constant, returns the value of PI (3.14...) # <<==================
# import math
# x = math.pi

# print(x)

# sqrt
# pi
# ceil
# floor

# ====================================================== ||
# //////////////////////>>>>  End <<<<////////////////// ||
# ====================================================== ||


# ====================================================== ||
# //////////////////////>>>  Json <<<<////////////////// ||
# ====================================================== ||

# JSON (JavaScript Object Notation) 
# JSON = a way to store and send data

import json

# Convert from JSON to Python

# some JSON:
# If you have a JSON string, parse it using the json.loads() method.

# x = '{ "name":"John", "age":999, "city":"New York"}'
# parse x:
# y = json.loads(x)
# the result is a Python dictionary:
# print(y["age"])

# x = '{ "name":"John", "age":999, "city":"New York"}'
# y = json.loads(x)
# print(y["name"])

# a = '{"model":"BMW", "year":"1992"}'
# b = json.loads(a)
# print("the model of car is ",b["model"])

# /////////////////////////////////////////////////
# Convert from Python to JSON
# by using the json.dumps() method.

# a Python object (dict):

# x = {
#     "name":"Hos",
#     "age":20,
#     "xs":"ld"
# }
# Converting to json
# y = json.dumps(x)
# print(y)

# x = {
#     "name":"Hos",
#     "age":20,
#     "xs":"ld"
# }

# y = json.dumps(x)
# print(y)

# from json to python is json.loads
# from python to json is dumps

# //////////////////////////////////////
# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
# ///////////////


# ====================================================== ||
# //////////////////////>>>  RegEx <<<<///////////////// ||
# ====================================================== ||


# re is build in package

import re
# # EX:Search the string to see if it starts with "The" and ends with "Spain“.
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$",txt)
# print(x)

# ////////////////
# findall() function returns a list containing all matches

# t = "the rain in spain"
# x = re.findall("ai",t)
# print(x)
# //////////////
# Search() function 
# If there is more than one match,
# only the first occurrence of the match will be returned.

# txt ="the rAin in the spain"
# x = re.search("a",txt,re.IGNORECASE)
# print(x)

# /////////////
# Split()
# The split() function returns a list ,where the 
# string has been split at each match.
# txt ="the rAin in the spain"
# x = re.split("\s",txt)
# print(x)

# sub()
# The sub() function replaces the matches with the text of your choice.
# t = "The rain in spain"
# x = re.sub("a","A",t)
# print(t)
# print(x)

# /////////////////////////////////
# /\/\/\/\/Metacharacters/\/\/\/\/\
# /////////////////////////////////
# Metacharacters are characters with a special meaning

# []
#Find all lower-case characters alphabetically between "a" and “z":
# import re
# txt = "The rain in Spain"
# x = re.findall("[a-x]", txt)
# print(x)

# /////////////////////
#Find all digit characters:
# import re
# txt = "That will be 59 dollars"
# x = re.findall("\d", txt)
# print(x)
## Output: ['5', '9’]
# /////////////////////////

# Any character (except newline character)
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# import re
# txt = "hello planet"
# x = re.findall("he..o", txt)
# print(x)

# /////////////////////
# ^ - starts with
#Check if the string starts with 'hello':
# import re
# txt = "hello planet"
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")

# ///////////////////

# $ -Ends with 
# #Check if the string ends with 'planet':
# import re
# txt = "hello planet"
# x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")
# #Output: Yes, the string ends with 'world’


# ///////////////////////
# #* - Zero or more occurrences
#Search for a sequence that starts with "he", 
# followed by 0 or more  (any) characters, and an "o":
# import re
# txt = "hello planet"
# x = re.findall("he.*o", txt)
# print(x)


# ////////////////////
## + - One or more occurrences
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
# import re
# txt = "hello planet"
# x = re.findall("he.+o", txt)
# print(x)
# Output: ['hello']

# ///////////////////

# ? - Zero or one occurrences
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
# import re
# txt = "hello planet"
# x = re.findall("he.?o", txt)
# print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o“.
# Output:[]

# //////////////
# {} - Exactly the specified number of occurrences
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# import re
# txt = "hello planet"
# x = re.findall("he.{2}o", txt)
# print(x)
# Output:  ['hello’]


# /////////////////////
# | - Either or
#Check if the string contains either "falls" or "stays":
# import re
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("falls|stays", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# Output: ['falls’], Yes, there is at least one match!

# //////////////////////////


# ====================================================== ||
# ///////////////>>>  Special Sequences <<<<//////////// ||
# ====================================================== ||

# A special sequence is a \ followed by one of the characters 
# in the list below and has a special meaning.



# \A - Returns a match if the specified characters are at 
# the beginning of the string.
# import re
# txt = "The rain in Spain"
# #Check if the string starts with "The":
# x = re.findall("\AThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# ///////////////////////
# \b - Returns a match where
# the specified characters are at the beginning or at the end of a word

# import re
# txt = "The rain in Spain"
# #Check if "ain" is present at the beginning of a WORD:
# x = re.findall(r"\bain", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# # Output: [],No match
# import re
# txt = "The rain in Spain"
# #Check if "ain" is present at the end of a WORD:
# x = re.findall(r"ain\b", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# ////////////////////////
# ////////////////////////////////////////////////////////////////////

# ====================================================== ||
# ////////////////////>>>  SETS <<<<//////////////////// ||
# ====================================================== ||


# A set is a set of characters inside a pair of square brackets
# [] with a special meaning:


# ====================================================== ||
# ////////////////////>>>  PIP  <<<<//////////////////// ||
# ====================================================== ||

# Try Except
# In Python, the try-except block is a way to handle errors so your program doesn't crash.

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try and except blocks.


#The try block will generate an error, because x is not defined:
# try:
#   print(x)
# except:
#   print("An exception occurred")
# Output: An exception occurred

# # //////////////////////
# try:
#   print("2" +2)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# /////////////////////
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
# ///////////////////////////



# String formating

# You can add parameters inside the curly brackets to specify how to convert the value.
# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))


# {:.2f}👉 Means:
# “Format this number as a float with exactly 2 decimal places”
# ////////////////////////
# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))
# # Also, if you want to refer to the same value more than once, use the index number:
# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))


# # ////////////////////////////
# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, 
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))

# //////////////////////////////
# 



# ====================================================== ||
# //////////////>>>  File handlining  <<<<////////////// ||
# ====================================================== ||

# File Modes
# Complete List of File Modes
# "r" - Read - Default value. Opens a file for reading; throws an error if the file does not exist.
# "a" - Append - Opens a file for appending (writes to the end of the file), creates the file if it does not exist.
# "w" - Write - Opens a file for writing, creates the file if it does not exist.
# "x" - Create - Creates the specified file, returns an error if the file exists.
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g., images)
# “+” - Read and write mode

# Combinations:
# 'rb'  - Read binary
# 'wb'  - Write binary
# 'ab'  - Append binary
# 'r+'  - Read and write (no truncate)
# 'w+'  - Read and write (truncate)
# 'a+'  - Read and append
# 'rb+' - Read and write binary



# ///////////////////////////////////

# # Open()
# f = open('test.txt')
# f= open("test.txt", 'r')

# with open('test.txt', 'r') as file:
#     # Perform operations
#     content = file.read()
# File automatically closed after the block

#/////////////////////////////////
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file.
# "w" - Write - will overwrite any existing content.
# f = open("test.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# f = open("test.txt", "r")
# print(f.read())
# f.close()
 
# ////////////////////////////
# Open the file “test.txt" and overwrite the content.
# f = open("test.txt", "w")
# f.write("overwriting the existing file") 
# f.close()
# f = open("test.txt", "r")
# print(f.read())


# "x" - Create - will create a file, returns an error if the file exist.
# "a" - Append - will create a file if the specified file does not exist.
# "w" - Write - will create a file if the specified file does not exist.


# x =100
# def change():
#     global x
#     x =50
# change()
# print(x)    


# ====================================================== ||
# /////////////////>>>  Revision  <<<<////////////////// ||
# ====================================================== ||




#    ======================================================||||===\/\/\/\/\/\/\\/\/\/\
#   1 %A-Weekday, full version                             ||||===\/\/\/\/\/\/\\/\/\/\                          
#   2 %a - Weekday, short version                          ||||===\/\/\/\/\/\/\\/\/\/\
#   3 %B-Month name, full version                          ||||===\/\/\/\/\/\/\\/\/\/\
#   4 %b-Month name, short version                         ||||===\/\/\/\/\/\/\\/\/\/\
#   5 %d-Day of month 01-31                                ||||===\/\/\/\/\/\/\\/\/\/\
#   6 %M-Minute 00-59                                      ||||===\/\/\/\/\/\/\\/\/\/\
#   7 %m-Month as a number 01-12                           ||||===\/\/\/\/\/\/\\/\/\/\
#   8 %Y-Year, full version                                ||||===\/\/\/\/\/\/\\/\/\/\
#   9 %y-Year, short version, without century              ||||===\/\/\/\/\/\/\\/\/\/\
#   10 %w-Weekday as a number 0-6, 0 is Sunday             ||||===\/\/\/\/\/\/\\/\/\/\
#   11 %H-Hour 00-23                                       ||||===\/\/\/\/\/\/\\/\/\/\
#   12 %I-Hour 00-12                                       ||||===\/\/\/\/\/\/\\/\/\/\
#   13 %p-AM/PM                                            ||||===\/\/\/\/\/\/\\/\/\/\
#   14 %S-Second 00-59                                     ||||===\/\/\/\/\/\/\\/\/\/\
#   15 %j-Day number of year 001-366                       ||||===\/\/\/\/\/\/\\/\/\/\ 
#    ======================================================||||===\/\/\/\/\/\/\\/\/\/\





# ====================================================== ||
# ///////////////>>>  MATH MODULE <<<<////////////////// ||
# ====================================================== ||

# Built in MAth Functions
# The min() and max() functions can be used 
# to find the lowest or highest value in an iterable.

x= min(3,1,5)
y = max(2,45,6)
print("The minimal value is " , x , "And the maximal value is" , y )

# Output:The minimal value is  1 And the maximal value is 45


# abs() < == function returns the specified number's absolute positve value
x= abs(-2.34)
print(x) 
# Output:2.34

# pow(x,y) <== Function returns the value of x to the power of y ==> (x^y) 
# x = > the number |  y = > how much time it will be multiplied 
x =pow(2,3)
print(x)
 
 
print("MATH MODULE =>")
#  MATH MODULE 
import math
# The math.sqrt() method for example, returns the square root of a number.
x = math.sqrt(49)
print(x)

# math.ceil() ==> method rounds a number upwards to its nearest integer.

x = math.ceil(2.3)
print(x)

# math.floor() ==>method rounds a number downwards to its nearest integer 
# and returns the result.

y = math.floor(2.3)
print(y)


# The math.pi constant, returns the value of PI (3.14...)
import math # First 
x= math.pi
print(x)


# ====================================================== ||
# ////////////////////>>>>  JSON  <<<<////////////////// ||
# ====================================================== ||

# 