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

import datetime as dt

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
    
    
# REgEx functions 
# Build in   
# Findall functions returnes a list containing all matches   
# search Returns a Match object if there is a mtch anywhere in the string
# split Return a list where the strig has been split at ecah match 
# sub Replaces one or many matches with s string 


# Findall()
# import re 
# x = "The rain in Spain and gain and spain"
# y = re.findall("a",x)
# print(y)
# print(type(y))
# print(len(y))


# Search()
import re
