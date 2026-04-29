# i = -1 
# while i <6:
#     i += 1
#     if i==3:
#         continue
#     print(i)

# def hello(x):
#       pass
# hello(3)

# n1=int(input("Enter n1 value:"))
# n2=int(input("Enter n2 value:"))
# opr=input("Enter your operator")
# def add(n1,n2):
#     print(n1+n2)
# def sub(n1,n2):
#     print(n1-n2)
# def mul(n1,n2):
#     print(n1*n2)
# def div(n1,n2):
#     print(n1/n2)

# if opr=="+":
#     add(n1,n2)
# elif opr=="-":
#     sub(n1,n2)
# elif opr=="*":
#     mul(n1,n2)
# elif opr=="/":
#     div(n1,n2)
    




    # new topic Class
# class MyClass:
#     x = 5
# print(MyClass)
    

# class human:
#     name = "Galety"
# print(type(human))
    
    
# /////////////////////////////////////////
    
    
# class human:
#     legs = 2
#     hands = 2 
#     eyes = 2  
#     nose = 1
#     ears = 2
   
# galety = human()

# print(galety.legs)
# print(galety.hands)



# /////////////////////////////////////////


# class hayder:
#     money ="200000$"
#     cars = 2
#     house = 1

# class mom:
#     cash = "10000$"
#     gold= "1"
        
# zafar = hayder()
# md = mom()


# print(zafar.money)
# print(md.gold)


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age     


# p1= person("name:Galety","age 52",)
# p2= person("name:Rafi","age 41")
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

# print("---------------------------------------------------")

# class haydar():
#     def __init__ (self,money,car,house):
#         self.mony=money
#         self.car= car
#         self.house =house
# zafar = haydar("100$","Laceti","Gagarin house")
# md = haydar("5000$","BMW","Rudaki")

# print(md.house)

# print("---------------------------------------------------")


# print("+-------+-----+-----------+")
# print("| Name  | Age | City      |")
# print("+-------+-----+-----------+")
# print("| Ali   | 20  | Tashkent  |")
# print("| Sara  | 22  | Samarkand |")
# print("+-------+-----+-----------+")



# class parents():
#     def __init__(self,m,h):
#         self.m = m
#         self.h = h
# child = parents('100$', 'x')
# child2 = parents('100$', 'y')
# print(child.m)
# print(child2.m)


# print("---------------------------------------------------")
# 2.06.2026
# New Topic
# Modify object properties


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age     


# p1= person("name:Galety","age 52",)
# p2= person("name:Rafi","age 41")


# p1.name = "Mohammed"

# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

# print("---------------------------------------------------")

# Delite object properties
# class person:
#     def __init__(self,money,car,house):
#         self.money = money
#         self.car= car      
#         self.house=house

# zafar = person("100$", "Car","House")
# md = person("500$", "laceti","big house")
# print("Before-Zafar properties")
# print(zafar.money, "|""\t\t", zafar.car, "|""\t\t",zafar.house)

# del zafar.money


# print("---------------------------------------------------")
# print("After-Zafar properties")
# print("none" ,"|""\t\t",zafar.car,"|" "\t\t",zafar.house)
# print(zafar)


# Empty class
# class SIUT:
    # pass
# if we write pass it doesn't show errors


# /they are the same but name is different
# pop )==> functions
# oop )==> metters for expmle (__init__)
# class has obeject ,properties, metters



# new topic
# inheretance )==> наследство 
# class hydar:  is Base class (Father class)
        # some property(x,y,z)
# class zafar: is derived class) (child class)
# if parent class has some properties the child class can also have 
# access to those properties and this colled as (Inheretance)
# class haydar:
#     def __init__(self,m,h): 
#         self.m =m
#         self.h= h
        
#     def hello(self): #metter
#         print(self.m,self.h) 
        
#     def bye(self):
#         print(self.h)
    
    
          
# child1 = haydar("100%","Gagarin")

# child1.hello()
# child1.bye()


# Creating a child class
# class haydar:
#     def __init__ (self,m,h): # m and h are properties
#         self.m =m
#         self.h= h
        
#     def hello(self): #metter
#         print(self.m,self.h) 
        
#     def bye(self):
#         print(self.h)
    
# class zafar(haydar):
#         def __init__ (self,zm,zh):
#             self.zm = zm 
#             self.zh = zh 
#         def zjob(self):
#             print(self.zm)
#             print(self.zh)


# ///////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////




# 2.11.2026
# New topic

# class haydar:
#     def __init__ (self,m,h):
#         self.m =m
#         self.h= h
        
#     def hello(self):
#         print(self.m,self.h) 
        
#     def bye(self):
#         print(self.h)
    
# class zafar(haydar):
#         def __init__ (self,zm,zh):#              
#            haydar.__init__(self,zm,zh)#          <---------
           
# x = zafar ("100$","Motrid")
# x.hello()


# Super() Functions


# class haydar:
#     def __init__ (self,m,h):
#         self.m =m
#         self.h= h
        
#     def hello(self):
#         print(self.m,self.h) 
        
#     def bye(self):
#         print(self.h)
    
# class zafar(haydar):
#         def __init__ (self,zm,zh):#             
#            super().__init__ (zm,zh)#             <---------we don't need self
           
# x = zafar ("100$","Motrid")
# x.hello()



# Add properties 
# class haydar:
#     def __init__ (self,m,h):
#         self.m =m
#         self.h= h
        
#     def hello(self):
#         print(self.m,self.h) 
        
#     def bye(self):
#         print(self.h)
    
# class zafar(haydar):
#         def __init__ (self,zm,zh,zc):         
#            super().__init__ (zm,zh)
#            self.zc = zc 
#         def wife(self):
#             print("I am going to marry Anora" )
                  
# class md (haydar):
#     # pass
#     def __init__ (self,mm,mh,mj):
#         super(). __init__(mm,mh)
#         self.mj = mj 
        
        
# a = haydar('1000$','Rudaki')          
# x = zafar ("100$","Motrid",'BMW 5 Competision ƪ(˘⌣˘)ʃ')
# y =md ('20000$',"gagarin","Developer")
# print(x.zc)
# print(y.mj)
# print(a.h)

# # a.hello()
# x.hello()



# MAking list an iterbale elemnts one by one

# l = [10,20,30]
# b = iter(l)
# print(next(b))
# print(next(b))
# print(next(b))


# we can make string as a iterable
# name = 'Husan'
# b = iter(name)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# Colimorphesm 


# Class is blue print 

# class human():
#     def __init__(self,head,arms,lags):
#         class Galety():
#             def __init__(h3):
#                 x = Galety("h1","a","l",'a','d')
# print(Galety)


                # NEW TOPIC---------------------- 
                # 2.13.2026----------------------
                # Polymorphism-------------------



# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
# def move(self):
#     print("Drive")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
# def move(self):
#     print("Drive")     
    
# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
# def move(self):
#     print("Drive")     
    
    
# car1 = Car("Ford", "Mustand")#Create an object  
# boat1 = Boat("Ibiz", "Touring 20")#Create an object
# plane1 = Plane("Boeing", "747")#Create an object
        
# for x in(car1,boat1,plane1):
#     x.move()


# # ////////////////////////////////////////////////////////

# class Vehicle():
#     def __init__ (self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Move")
#         class Car(Vehicle):
#             pass  
# class Boat (Vehicle):
#     def move(self):
#                 print("Sail")
# class Plane (Vehicle):
#     def move(self):
#                 print("Fly")
                
# for x in(car1,boat1,plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()



# NEW TOPIC
# SCOPE
# x = 300

# def hell(): 
#     global x   
#     x = 200
# hell()
# print(x)



# Function insede the function is recursion!!!!!!
# def myf():
#     x = 300
#     def myinnerf():
#         print(x)
#     myinnerf()
# myf()


# def uzb():
#     x =300
#     def tashkent():
#         print(x)
#         global y
#         y = 500
#     tashkent()
    
#     def samrkand():
#         print(x)
#     samrkand()
        
# uzb()
# print(y)

# Naming Variables


# x =300
# def hello():
#     x= 200
#     print(x)
    
# hello()
# print(x)



# MODULES 



# import untiteled1
# print('i am importing')
# print(ai.ai["sname"])


# new topic 2.18.2026

# Datetime
# print('=-----------------------=')
# import datetime as dt
# x = dt.datetime.now()
# print(x)
# a = x.year
# print('=------------------------=')
# print(x.strftime("today is %A")) # str = string , f = format, time = time

# # Creating date objects


# import datetime as dt
# y = dt.datetime(2008,4,5)
# print(y)
# print(x-y)
# b=y.year
# print(a-b)


# ////////////// Strinftime() method , dates will be converted to string format 
# import datetime as dt
# x = dt.datetime.now()
# print(x.strftime("%A")) # % here means i want to present week

# import datetime as dt

# /////////////////////////////// 
# %B shows months
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%B"))


# ////////////////////////////
# numbers of a week
# %w  index number of a week days
# days   :sun mon tus wed thur fn sat
# indexes:0   1   2   3   4    5  6   

# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%w"))

# /////////////////////
# %d shows date
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%d"))



# /////////////////////
# %m shows number of month
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%m"))



# /////////////////////
# %y or %Y shows year 
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%Y"))


# /////////////////////
# %H  shows hours  00-23
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%H"))

#           <=\\
#             \\==\\
#                  \\=>

# /////////////////////
# %I  shows hours 00-12
# y = dt.datetime.now()
# print(y.strftime("%I"))

# ////////////////////////
# %p shows , wether hour is pm or am
# import datetime as dt
# y = dt.datetime.now()
# print(y.strftime("%p"))


# ////////////////////////
# %M shows minutes
# y = dt.datetime.now()
# print(y.strftime("%M"))

# ////////////////////////
# %S shows seconds
# y = dt.datetime.now()
# print(y.strftime("%S"))

# ////////////////////////
# %j  day in a year
# y = dt.datetime.now()
# print(y.strftime("%j"))
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# new Module

# Matimcatical related functions
# Math


# max find maximum value
# x = [10,20,30,44557,76543,754,267545,556752,5,9,87,98765432,123456789,7,557755443,8756,83,685,5678,3567,3567,36789,57,65,2986,75645,765334,5645436,76543,876543,76545,65,567,455667,4567,56,6556]
# print(max(x))


# abs means absolute
# x = [1,34,-45]
# print(abs(x[2]))

# pow help to find any degree
# print(pow(2,3))

# previese things are build in functions
# 

# Math module

# math with "sqrt" finds the sqeare of any number 
# import math
# print(math.sqrt(49))


# math ceil() this is a  function is for sounding purpose 
# import math 
# ceil for upword direction
# print(math.ceil(1.6))
# floor for downword direction
# print(math.floor(1.6))

# math.pi => 3,14
# import math
# print(math.pi) 
# 
# New Topic
# Json
# java script object rotaions
# to store and exchange data from one system to another system 
# loading the page calls buferring
# passing means scanning or compiling 
# Syntaxis is important
# json format is format of strings
# json.loads()

# converting json to python
# import json
# x = '{"name":"John","city":"SKD"}'
# print(x)
# print(type(x))
# y = json.loads(x)
# print(y)
# print(type(y))
# print(y["name"])

# converting python to Json

# we can canvert any data type

import re

# RegEx =======> "re" (in code)
# Regular expressions
#  spining pen 

# import re 
# x = "The rain in Spain"
# y= re.search("^The.*Spain$",x)
# # print(y)
# if y:
#     print('Yes! we have the match')
# else:
#     print("No match")
    
    
#  //////////////////////////////////////////////////////////////////////////////////////////////
#  //////////////////////////////////////////////////////////////////////////////////////////////
#  //////////////////////////////////////////////////////////////////////////////////////////////
#  //////////////////////////////////////////////////////////////////////////////////////////////
    
# REgEx functions 
# Build in   
# Findall functions returnes a list containing all matches   
# search Returns a Match object if there is a mtch anywhere in the string
# split Return a list where the strig has been split at ecah match 
# sub Replaces one or many matches with s string 


# Findall() will search all
# import re 
# x = "The rain in Spain and gain and spain"
# y = re.findall("a",x)
# print(y)
# print(type(y))
# print(len(y))


# Search() will search first 
# import re
# x = "The rain in Spain and gain and spain"
# y = re.findall("ai",x)
# print("The fist ai stric is located in position:",y.start()) # start() indicates the exact location




# IGNORECASE )==> ignores coase sensitev txt
# import re
# x = "The rAin in Spain and gain and spain"
# y = re.findall("ai",x,re.IGNORECASE)
# print("The fist ai stric is located in position:",y.start()) # start() indicates the exact location

# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=>/
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=>/
# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=>/
# />,'[*$#!!@)(*%&%$><:{}"?|\?/~~~~~~~~~|?"><:{+(&^%$
# 2.25.2026
# New topic





# Split <========

# txt= "The rain un Spain"
# x =re.split('\s',txt)
# print(x)
# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])


# for i in txt:
#     print(i)
    
# Sub function =====> substitude means replace
# x = "SIUT"
# # replace(searching,replacing,source)
# # replace(\s),9,x)
# x = re.sub("S","SAMARKAND",x)


#//////////////////////////
# |s means space   <<<<<<<|
#//////////////////////////


# Metacharacters 
# First metchacharacter  ===> [] (this is polymorphisim)
# [] ==> means container where we can store something , this is a set of characters
# this finds all lower-case characters in alphabetically
# between'a' and 'z'

# txt=("the eain in Spain")
# x = re.findall("[A-Z]",txt)
# print(x)

# Singals a specia sequence
# txt=("That will be 59 dollars")
# # Find all digit characters
# x = re.findall("\d",txt)
# print(x)


#  next metacharcter is dot(.) means any character ==> exept newline character
# txt=("hello planet hebao")
# Find all digit characters
# x = re.findall("he..o",txt)
# print(x)
# it works because the length is correct 
# and published characters at the start and end are correct




# metacharacter (^) cap sybmole===> forces any chacter to begin 1st in the line 
# t ="hello planet"
# x = re.findall("^hell",t)
# print(x)



# Next metachaeacter ($) forces any chacter to be at the end in the line 
# t ="hello planet"
# x = re.findall("^hello",t)
# x = re.findall("planet$",t)
# print(x)




# USIng many metacharacters
# t ="The rain in Spain"
# x = re.search("^The.*Spain$",t)
# print(x)
# if x:
#     print("We have a match")
# else:
#     print("No match")
    
    
# Rearching any number of charcaters with (. and *)
# t ="The rain in Sayfiyev Husan"
# x = re.findall("S.*n",t)
# print(x)

# next metacharacter is (+) means one or more 
# t ="Sun"
# x = re.findall("S.+n",t)
# print(x)



# next metacharacter is (?) means 0 or one occurences needed
# t ="Sn"
# x = re.findall("S.?n",t)
# print(x)


# next metacharacter is ({}) exactly the specidid number of occurrences


# New tipic 3.4.2026
# Metacharacters

# txt = "The rain in Spain"
# x = re.findall('he.{3}o',txt)
# print(x)


# txt = "helal hella hala hello worl"
# x = re.findall("helal | hello ",txt)
# print(x)


# Special sequeances ==> checks if the string starts with "The"

# txt = "The rain in Spain"
# x = re.findall("/A The", txt)
# print(x)


# \b returs a match where the specified characyers are at the beginning or at the end of a word(the
# "r" in the beffining is making sure that the string is being treated as a "row")
# txt = "The rain in Spain"
# x = re.findall(r"\brain", txt)
# print(x)

    
    
    
# \d 

# txt = "The rain in Spain2"
# x = re.findall("\d", txt)
# print(x)



# \s to find white spaces we need to use spaces and \S
# txt = "The rain in Spain2"
# x = re.findall("\S", txt)
# print(x)



# \w returns a match contains any word characyers from A to Z only
# txt = "The rain in Spain2"
# x = re.findall("\w", txt)
# print(x)


# \W retuerns a match where  word does not have any caracters from a to z 
# txt = "The rain in Spain2"
# x = re.findall("\\W", txt)
# print(x)





# # 
# txt = "The rain in Spain2_"
# x = re.findall("2\Z", txt)
# print(x)



# Sets 
# A set is a set of characyers inside a pair of sqeare breackets [] with a special meaning
# arn  -Returns a match where one of the 

# txt = "The rain in Spain2_"
# x = re.findall("[arn]", txt)
# print(x)




# Range from [a-n]

# txt = "The rain in Spain2_"
# x = re.findall("[a-n]", txt)
# print(x)




# [^] avoids charactres listen in [^]
# txt = "The rain in Spain2_"
# x = re.findall("[^a]", txt)
# print(x)



# txt = "The rain in Spain2_"
# x = re.findall("[0-1]", txt)
# print(x)


# returning bor big letter and small
# txt = "The rain in Spain2_"
# x = re.findall("[a-zA-Z]", txt)
# print(x)

# searchs only + 
# txt = "The rain in Spain2_"
# x = re.findall("[+]", txt)
# print(x)


# PIP insalls packages/preferred installer profram 
# import camelcase as cc

# c = cc.CamelCase()
# x = c.hump("hellow world")
# print(x)


# ////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////


# Exceptions hendling
# Try Except
# try:
#     print(x)
# except:
#     print("An exception occurred")


# 3.6.2026

# try:
#     x =10
#     print(x)
#     print(y)
# except NameError:
#     print("Variable 'x' is not definde")
    
# try: /
    # a = 10/0
# except ZeroDivisionError: #  <====== THis si built in exception function ) for raseing the error
    # print("You cannot divide by zero")

# try:
#     int('abc')
# except ValueError:
#     print("Cought a valueError: Cannot convert 'abc' to an integer")


# try:
#     a =10
#     b = "5"
#     x =a +b
# except TypeError:
#     print("Caught a TypeError: Cannot add integers")


# try:
#     a = {
#         "name":"Jhone",
#         "Age":30,
#         "City":"New York"
#     }
#     print(a["nme"])
# except KeyError:
#     print("key not found in the dictionary")
    
    
# try:
#     open("new-topic.py","r")
# except  FileNotFoundError:
#     print("Finle not dound")
    
    
# try:
#     a =10
#     b =20
#     c =a+b
# except NameError:
#     print("Varable 'd' is not definde")


# try:
#     number  = int(input("Enter a number: "))
#     result = 10 / number 
#     print(f"Rsult is {result}")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("That is not aa valid number !")
    

# try:
#     open("new-topics.py",'r')
# except FileExistsError:
#     print("Fie not found")
# else: 
#     print("File opened succussfully")
# finally:
#     print("This block will alwaus execute , regardless of excetions ")
    
    
# x = -1 
# if x < 0:
#     raise Exception('Neagtive value is not allowed')
        
    

# 1. Define your custom exception

# class InvalidInput (Exception):


# String formating 
# price  = 49 
# txt = "The price is {} dollars"  #{} < ==colled  placeholders
# print(txt.format(price))



# 3.11.2026

# price = 49 
# order = 3
# txt = "The price of each mouse is {} dollars & i want to order {} items"
# print(txt.format(price,order))


# Numbers formating with desimal point (.000)
# :.2f ===> means two fractional points
# price = 49 
# order = 3
# txt = "The price of each mouse is {:.2f} dollars & i want to order {} items"
# print(txt.format(price,order))



# Index numbers 
# price = 49 
# order = 3
# total_price = price * order
# txt = "The price of each mouse is {0:.1f} dollars & i want to order {1:.2f} items and total price is {2:.2f}"
# print(txt.format(price,order,total_price ))



# ///////////////////////////////////////
# NEW TOPIC, IMPORTANT!!!
# File Handling



# old model of openning files
# f = open("TEST.txt","r")    
# print(f.read())
# f.close()  <==\\
#                \\ ==> we need to close file 



# ////////////
# Buffer freshing 

# new model of openning files
# with open ("TEST.txt", "r") as f:
#     content = f.read()
#     print(content)
    
    
# with open('C:\SIUT\Java_lessons\s.txt','r') as file:
#     print(f'File name:{file.name}')
#     print(f'File mode:{file.mode}')
#     print(f'Is the file closed:{file.closed}')
#     print(f'File endcoding:{file.encoding}')
# file.close()
# print(f'Is the file closed:{file.closed}')


# # Creating and storing a data
# name = input("Enter ur name:")
# with open ('test.txt','w') as file:
#     file.write(f'User name: {name}')
    


# p = int(input("Enter principle amount:"))
# t = int(input("Enter time:"))
# r = int(input("Enter rate of interest:"))
# with open("test.txt" ,'a') as file:
#     file.write(f'Principal amount: {p}\n')
#     file.write(f'Time period: {t}\n')
#     file.write(f'Rate of interest: {r}\n')
#     file.write(f'Simple interest: {(p*t*r)/100}\n')

# p = int(input("Enter principle amount:"))
# t = int(input("Enter time:"))
# r = int(input("Enter rate of interest:"))
# with open("test.txt" ,'a') as file:
#     file.write(f'Principal amount: {p}\n')
#     file.write(f'Time period: {t}\n')
#     file.write(f'Rate of interest: {r}\n')
#     file.write(f'Simple interest: {(p*t*r)/100}\n')




# ///////////////////
# if foder is empty it will be deleted!
# import os


# if os.rmdir("hi"):
#     print("This was not empty")
# else:
#     print("It was empty")
    
# ////////////////////////////
# NumPy ==> Numerical Python ===
#                               \\
#                                 ==> Here we use arreys 


# import numpy as np
# a =np.array((10,20,30))

# print(type(a))
# print((a))

# ///////////////////
# Arrays
# import numpy as np
# a =np.array((10,20,30)) # < ==== every value is 0-d array  
# print(type(a))

# One_d array
# import numpy as np
# a =np.array((10,20,30)) # < ==== collection of 0-d arrays colled one-d array
# print(type(a))


# 2-D arrays ===> collection of one-d arrays colled 2-d arrys
# import numpy as np
# a =np.array([[10,20,30],[40,50,60],[70,80,90]])   # < ==== collection of 0-d arrays colled one-d array
# print(type(a))
# print((a))
# print(a.ndim)



# 3-D arrays ===> collection of two-d arrays colled 3-d arrys
# import numpy as np
# a =np.array([[[10,20,30],[40,50,60],[70,80,90]],[[100,110,120],[130,140,150],[160,170,180]]])   # < ==== collection of 2-d arrays colled Three-d array
# print(type(a))
# print(a.ndim)


# ndim show the quantity of dimentions


# Access array elements

# ////////////////////////////////////////////////////////////////
#                                                                |
#                                                                |
#                                                                |
# After midterm exams                                            |
#                                                                |
#                                                                |
#                                                                |
#/////////////////////////////////////////////////////////////////


import numpy as np
# Access array elements
# a = [10,20,30,40]
# print(a[1], a[2])


# arr =np.array[{1,2,3,4}]

# print(arr[2]+ arr[3])

# a = np.array([[1,2],[3,4]])
# print(a)



# w= np.array([[10,20,30],[40,50,60]])
# print(w[1,2], w[2,1])

# l = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


# print(l[0,1,1])
# array, row , column
# print(l[1,1,1])



# a=np.array([[1, 2],[3, 4]])

# b=np.array([[5, 6],[7, 8]])

# result = np.zeros((2, 2), dtype=int)

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[i][j] = a[i][j] + b[i][j]

# print(result)

# for i,j in[(a,b)]:
#     print(i+j)
#     break


# from numpy import random
# x= random.randint(5)
# print(x)


# 1d array
# wd = random.randint(26,size=(5))
# print(wd)

# 2d array
# wd = random.randint(26,size=(5,3))
# print(wd)


# 
# wd = random.rand(26)
# print(wd)


# a = random.rand(1,3)*100.00
# print(a)


#Alternative Methods
# x = random.uniform(0,199,(3,5)) 
# print(x)







# NEw topic new day

# generate random from array

# x= random.random((3,5))* 100
# print(x)



# from numpy import random
# a= [1,2,3,4,5]
# print(random.choice(a))

# X =random.choice([3,4,5,6],size=(3,5))
# print(X)

# import numpy as np


# Making zero matrix
# n1 = np.zeros((2,3))
# print(n1)
# Sao12345



# MATRIX WITH MY DESIRED NUMBER
# a =np.full((2,3),7)
# print(a)


# Initializing numpy aeeay within
# a= np.arange(5,10)
# print(a)




# a= np.arange(100,300,500)
# print(a)

# 

# 
# from random import random
# a =np.random.randint(1,10,5)

# print(a)

# np = np.array([[1,2,3,4],[5,6,7,8]])
# print(np)

# print(np.shape)

# print(np.ndim)



# np.shape =(4,2)
# print(np)


# Sum two arrays
# nl = np.array([1,2])
# na = np.array([3,4])
# print(nl.sum())
# print(na.sum())

# print(np.sum([nl,na], axis = 0))
# print(np.sum([nl,na], axis = 1))


# /=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
# from numpy import vstack
# from numpy import hstack
# nl =   np.array([1,2])
# # na =   np.array([3,4])
# na2 =  np.array([5,6])
# np.vstack((nl,na,na2))
# print(np)
# M = np.vstack((nl,na,na2))
# print(M)
# n5 = np.hstack((nl,na,na2))
# print(n5)
# 
# 
# 
# 
# Column 
# n6= np.column_stack((nl,na,na2))
# print(n6)


# 
# ======================================|
# ======>>|Random Distribution|<<=======|
# ======================================|

# Random data distribution ||||

# from numpy import random
# x= random.choice([3,5,7,9],p =[0.1,0.2,0.3,0.4], size= 10)
# print(x)

# Marker Color
import matplotlib.pyplot as plt
import numpy as np
# plt.plot(x,y,ms =20, mec = "red",mfc = "yellow",
#          ls = "dashed",marker ='3',color= 'green'
#          ,lw= 2, 
#          )
# font1 = {'family':"serif",'color':"blue","size":20}
# font2 = {'family':"serif",'color':"darkred","size":15}
# plt.title('age vs years',fontdict=font1,loc = 'left', color = 'purple')
# plt.xlabel('Age', fontdict =font2)
# plt.ylabel('Years',fontdict = font2)
# plt.grid(axis = 'x',color = 'green',linestyle='--')

# x = np.array([5,25])
# y = np.array([5,5])
# plt.subplot(1,3,1)
# plt.plot(x,y)
# plt.title('Line Graph')

# a = np.array([15,25])
# b = np.array([25,50])
# plt.subplot(1,3,2)
# plt.plot(a,b)
# plt.title('2nd Graph')

# e = np.array([15,25])
# f = np.array([25,50])
# plt.subplot(1,3,3)
# plt.plot(e,f)
# plt.title('Last Graph')
# plt.suptitle('This is  mine')

# x = np.array([1,2,3])
# y = np.array([8,9,10,11,12,13,14])
# color = ["red",'blue','green','yellow','cyan','magenta','orange']
# color = [0,10,20,30,40,50,60]

# plt.title("Scatter Plot")
# x = np.random.randint(100, size =(100))
# y = np.random.randint(100, size =(100))
# size = 10 * np.random.randint(100,size = (100))
# x = ["hussein", "Ali", "Omar","Youse"]
# y = [90,20,60,34]
# z =np.random.normal(12,34,160)
# color = ["red",'blue','green','yellow']
# x2 = np.array([16,22,31,43,55,61,7])
# y2 = np.array([8,9,10,11,12,13,14])
# color = ["red",'blue','green','yellow','cyan','magenta','orange']
# plt.scatter(x2,y2, color = color)
# plt.scatter(x,y,s = size ,alpha = 0.5, cmap = "nipy_spectral")
# plt.barh(x,y)
# plt.bar(x,y, color = color,width = 0.4)
# plt.hist(x,y, color = color,height  =0.5)
# l = np.array([8,2,4])
# ex  = [0.2,0,0]
# col = ["red","ble","gray","vsd"]
# plt.pie(x, labels=["a","b","c"], startline =180, explode = ex ,shadow=  True,colors = col)
# plt.legend(title = "Djdd", loc = "lower left")


# plt.pie(y)
# plt.title("Scatter Plot")
# plt.hist(z)
# plt.show()

# a11 = np.array([10,10,0,-10,-10,0,0,-5,-5,0,10])
# b11 = np.array([40,190,180,160,60,40,50,60,160,170,180])
# a12 = np.array([-15,25,25,-15,-15])
# b12 = np.array([30,30,40,40,30])
# a13 = np.array([0,10,10,0,0])
# b13 = np.array([0,0,30,30,0])

# plt.plot(a11,b11,color = "grey")
# plt.plot(a12,b12,color = "black")
# plt.plot(a13,b13,color = "black")
# plt.show(
    
# names = ["a", "a", "os", "Extra", "Extra2"]
# marks =[10,20,30, 25, 90]
# colors2 = ["red", "green", "blue"]
# widths = [0.1, 0.2, 1.2]
# # plt.barh(names, marks, color = colors2, height=widths)

# nums = np.random.normal(170, 10,250)
# # plt.hist(nums)
# # plt.show()

# plt.pie(marks, labels=names, startangle=90, counterclock=False, explode=[0.2,1,0.2,0.2,0.2], shadow=True, colors=["gold","brown", "red", "blue", "orange"])
# plt.legend(loc="lower left", title="Names")
# plt.show()




# ====================================================== ||
# ///////////////>>>>> Pandas Module <<<<<////////////// ||
# ====================================================== ||

# Stracture qeary lenguage , not programming language but datebase language.

# Single - dimensioanl data set
import pandas as pd
# a= pd.Series([1,2,3,4,5],index= ['a','b','c','d','e'])
# print(a)
# print(type(a))
# Index | Number |
# 0     |    1   |
# 1     |    2   |
# 2     |    3   |
# 3     |    4   |
# 4     |    5   |

# # ///////////////////////////
# q= pd.Series({"Snomber": "1","Sname" :"galety","Awp":"0"})
# print(q)


# Padnas with two dimantional dataset

# a = pd.DataFrame({"Sno":[1,2,3],
#                   "Sname":["Husan","Asalya","Husniddin"],
#                   "Prg":["CS","Al","AI"]})
# print(a)
# print(type(a))


# Pandas => data manupulations and data analysiz
# For this => Shape(),describe(), head(), tail();
# data schould be in exel or .csv , the last one is faster 
# Comma spareter format
# a =pd.read_csv('C:\SIUT\Python from scratch\covid\country_wise_latest.csv')
# print(a)
# print(type(a))
# ///////////////////

# df =pd.read_csv('C:\\SIUT\\Python from scratch\\covid\\country_wise_latest.csv')
# print(df.head())
# print(df.tail())
# =============/\/\/\/\/\/|=================>
df =pd.read_csv('C:\\SIUT\\Python from scratch\\covid\\country_wise_latest.csv')
# ========================
# Top 5 records
# print(df.head())

# Top 10 records
# print(df.head(10))

# Last 5 records
# print(df.tail())

# Last 10 records
# print(df.tail(10))
# ======================
# Passing index of the columns == iloc()
# print(df.iloc[0:3,0:3])
# ======================
# Passing index of the columns == loc()
# print(df.loc[0:3,['Country/Region','Confirmed',"New cases"]])

# ======================
# Passing the data inside table
# print(df[df["Country/Region"]=="China"])

# ======================
# Contitions
# a = df[(df["    " ]> 100) & (df["Country/Region" ]=="Algeria")]
# print(a)




# ====================================================== ||
# ////////////////>>>>>>> Tkiinter <<<<<<<////////////// ||
# ====================================================== ||
# 
# Kivy
# Python Qt
# wxPython

import tkinter as tk
from tkinter import ttk
# ttk is submodel of tkinter