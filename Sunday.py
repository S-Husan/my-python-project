# Revision
# Here we go again

# MODULE I

# x = 1 # Int
# y = 2.3 # Float
# z = 2j # Complex

# Type function (We use this to verify the type of opject)

# print(type(x)) int
# print(type(y)) float
# print(type(z)) complex

# Random function 
# import random
# print(random.randrange(1,20))

# import random
# print(random.randrange(1,30))

# Strings are Arrays 
# A single charcter is simply a string with a length of 1
# a = "Hello world"
# print(a[0:2])

# Looping through a String 
# Since string are arrays, we can loop through the characters in a 
# string with a "FOR" loop.

# for x in "Salom":
#     print(x)
    
# String Length 
# len() function 
# a = "I am from Samarkand"
# print(len(a))

# to Check string we use "IN"
# a = "I am from Samarkand"
# if 'Samarkand' in a:
#     print("Yes it is")
    
# Check if NOT
# a = "I am from Samarkand"
# print("from" not in a) 

# Slicing 
# you can return a range of characters by using the slice syntax.
# b = "hello now"
# print(b[0:4],b[6:8])

# Important TOPICS !!!
# Modefy Strings 

# 1 Upper() returns the string in upper case
# a = "Salom"
# print(a.upper())

# 2 Lower() returns the string in lowercase
# a = "HAYIR"
# print(a.lower())

# Remove whitespace
# 3 Strip() method removes any space from beginning or at the end
# a = " skak ee "
# print(a.strip())

# Replace String 
# 4 Replace() replaces string with another one
# a = "Hell aplla"
# print(a.replace("l","Bo"))
# print(a.replace('l','2'))
# print(a.replace('a','C'))

# Split string
# 5 Split()
# a = "Salom world"
# b = a.split(",")
# print(b)

# String Concatination 
# a = "hello, "
# b = "Word"
# c = a + b 
# print(c)

# String Fromat
# We can mix string and numbers by using format() method!
# 6 format()
# age = 17 
# Major = "CS" 
# txt = "Hi my name is husan and my age is {}, and i study at university and my major is {}"
# print(txt.format(age,Major))

# age = 12
# school= 1
# txt = "hi my age is {} ,a and i study at {}, school"
# print(txt.format(age,school))

# Module 2
# NEW TOPICS 

# 1 Copitalize()
# ml = "salom bu dunyo"
# print(ml.capitalize())

# 2 Casefold()
# ml = "SaloM Bu dUnyo"
# print(ml.casefold())


# 3 Cneter , mover elemet to center by using numbers 
# txt = 'THIS IS THE CENTER'
# a = txt.center(167)
# print(a)

# Count
# txt = ' i like red apple, green apple, and yellow apple'
# print(txt.count("apple"))
# print(txt.count("i"))
# BOOLEANS (True or False)
# print(10 < 9)   /False
# print(10 == 9)  /False
# print(10 > 9)   /True

# Example for this booleans
# a = 1
# b = 2
# if b > a:
#     print(True)
# else:
#     print(False)

# Function can return a boolean 
# def My_f():
#     return False
# print(My_f())


# MODULE 3 

# Build in functions ---> isinstance()

# x = 200
# print(isinstance(x,complex))
# print(isinstance(x,float))
# print(isinstance(x,int))

# NEW topic
# LIST items => Ordered , Changable (Mutable) ,Allow Dublications
# x = ["Apple","juce","cola"]
# print(x)

# Acces items in list becase they are indexed 
# x = ["Apple","juce","cola"]
# print(x[1])
# print(x[1-2])
# Using range of indexes in list 
# x = ["Apple","juce","cola"]
# print(x[0:2]) 

# Check if item exist 
# x = 'apple,banan ,cherry,pottaod'
# if "apple" in x:
#     print(True)
    
    
# MODULE 4

# Change the item value 
# c = [1,2,3,4]
# c[0]= 'First'
# print(c)
# ...................
# b =[2,3,4,5,8]
# b[2] = 'ASD'
# print(b)


#Change a range of item values 
# x = ['apple','banan','cherry']
# x[2:3] = ['a','b']
# x[0:2] = ["LAP","pal"]
# print(x)

# If you insert more items than you replace,-
# -the new items will be inserted where you specified,-
# -and the remaining items will move accordingly.

# p = ['a','s','f']
# p[0:2]= ['x','v','t','y']
# print(p)

# insert Items
# insert() method insertd an item at the specified index-
# ,and it doesn't replace any existing values in the list.
# x = ['apple','banan','cherry']
# x.insert(2,"Chocotela")
# print(x)

# x = [12,3,4,5]
# x.insert(1,"second is here")
# print(x)

# Append()
# To add an item to the end of the list, use the append() method.
# x = ['apple','banan','cherry']
# x.append("JUSEEE")
# print(x)


# extend 
# To uppend elements from another list to the current list,-
# use the extend() method.
 
# old = [1,2,3]
# new = [4,5,6]
# old.extend(new)
# print(old) 

# new.append(old)
# print(new)

# Add any iterable
# The extend() method does not have to append() lists;

# Remove Specified items
# remove()
# x= ['app','coll','pull']
# x.remove("app")
# print(x)
# x.remove("coll")
# print(x)


# Remove Specified Index  
# x= ['app','coll','pull']
# x.pop(0)
# print(x)  


# If you don't spesify the index, the pop() method removes the last item.
# x = [1,23,4,5,6,7]
# x.pop()
# print(x)

# del also removes the specified index.
# z = [12,5,6,4,2,5,4]
# del z[0]
# print(z)
# del z[2]
# print(z)

# Clear() method empties the list 
# The list remains, but without content
# z = [12,5,6,4,2,5,4]
# z.clear()
# print(z)

# LOOPS in LIST
# y = [1,3,4]
# for i in y:
#     print(i)
    
# Loop through the index number
# x = ['apple','orange','banana','cherry']
# for i in range(len(x)):
#     print(x[i])

# num = [1,2,3,4,5]
# for i in range(len(num)):
#     print(num[i])

# Revision just for me 
# loop throgh the list with for 
# x  = [1,2,4,5,3]
# for i in x:
#     print(i)
# LOOP throuh the list by using index number
# x  = [1,2,3,4,5,330]
# for i in range(len(x)):
#     print(x[i])

# MODULE 5
# Using while loop 
# ROOLS ===>
# ===>  You can loop through the list items by using a while loop.
# ===>  Use the len() function to determine the list length, 
# ===>  then start at 0 and loop your way through the list items 
# ===>  by referring to their indexes.
# ===>  Remember to increase the index by 1 after each iteration.

# x = ['apple','bnan','cherry']
# i = 0
# while i < len(x):
#     print(x[i])
#     i= i + 1

# i = 0
# while i  < len(x):
#     print(x[i])
#     i=+i
    
# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists.
# A shorthand for loop that will print all items in a list.
# y= ["apple", "banana", "cherry"]
# # [print(i) for i in y]


# Revision
# y= ["apple", "banana", "cherry"]
# [print(x) for x in y]

# y= ["apple", "banana", "cherry"]
# n = []
# for i in y:
#     if 'a' in i:
#         n.append(i)
# print(n)

# num = [1,2,3,411,331,'q']
# n = []
# for i in num:
#     if "q" in num:
#         n.append(i)
# print(n)

# Prictise
# for i in range(1, 21):
#     if i == 15:
#         print(f"{i}: You should stop here")
#         break
#     print(f"{i}: Going right")
#




# NEW TOPIC 

# # Iterable
# y = [x for x in range(10)]
# print(y) 

#Simple version =====>

# y = []
# for x in range(10):
#     y.append(x)
# print(y)


# Expression
# fr = ['app','sks','dd','wkd']
# newlist = [x.upper() for x in fr]
# print(newlist)
# Simple version =====>
# fr = ['app', 'sks', 'dd', 'wkd']
# newlist = []          # empty list
# for x in fr:          # take each word from fr
#     newlist.append(x.upper())  # make it uppercase and add to newlist
# print(newlist)

# f = ['111','222']
# na = []
# for x in f:
#     na.append(x.lower())
# print(na)


# Sort lists Alphanumerically
# x = ["d",'a','w','r','f','g','q' ]
# x.sort()
# print(x)

# sort() numerically
# x = [103,5,7,2,1,8,9,6]
# x.sort()
# print(x)

# reverse = True )=> to sort reversed sort()
# z = [2,5,6,7,3]
# z.sort(reverse= True)
# print(z)

# Case insensitive sort
# By default the sort() is case_sensitive, sorting all capital letters before lowercase letters.
# x = ['APplE','skd','cucumber','pineapple']
# x.sort()
# print(x)

# Case-insensitive sort function we use this 
# x = ['APplE','skd','cucumber','pineapple']
# x.sort(reverse = True)
# print(x)

# Reverse order
# The reverse() method reverses the current sorting order of the elements.
# x = ['banan','cucumber','potato','sosages']
# x.reverse()
# print(x)

# Copy a list 
# we use Copy() method
# x = [1,3,4]
# new = x.copy()
# print(new)

# Another way to make a copy is using list()
# x = [1,23,4]
# z = list(x)
# print(z)

# x = [35,6,6543,56,3]
# z = list(x)
# print(z)

# Join two lists by using + operator
# x = ['a','b','c','d']
# y = [1,2,4]
# z = x + y
# print(z)

# Another way to join two lists is by appending all the items from list2 into list1, one by one
# a = [12]
# b = [13,4,5]
# for i in b:
#     a.append(x)
    # “Put value at the end of list a.”
    # “Take the current number stored in i and put it into list a.”
# print(a)        


# or Use the extend() method to add list2 to the end of list1
# a = [232,3,5]
# b = [0,0,0]
# a.extend(b)
# print(a)

 
 
# MODULE 6
# Tuples
# They are used to store multple ites in a single variable.
# A tupel is a collection which is ordered and unchangeable.
# Tuples are written with round breackets().
# x = ("apple","banna","Cherry")
# print(x)

# Tuple Items
# Tuple items are ordered Unchangeable,and allow duplicate values


# Ordered means )==> that the items have a defined order,and that order will not change.

# Unchageable means  )==> that we cannot change, add or remove items after the tuple created 

# Allow duplicates
# x = ('a',"b",'a')
# print(x)

# Rule for tople 
# to type one object insie the tuple u need to put
# comma(,)after that otherwise Python will not recognize it as a tuple.
# t = ('apple',)
# print(t)

# Tuple length
# tuple = (1,2,3,4,5)
# print(len(tuple))


# Tuple constructor 
# x=("apple", "banana", "cherry")
# thistuple = tuple(x)
# print(thistuple)


# Access Tuple Items
# you can access tuple items by referring to the index number, -
# inside sqeare brackets.
# this = ('apple','banana','Cherry')
# print(this[2])


# negative indexing 0===> means start from the end (starts from -1)
# t = (1,2,3,4)
# print(t[-1])

# Range of Indexs
# You can choose where to start and were to end the range
# When specifing a range, the return value will ba a new tuple with the specified items.
# t = (1,23,4,5,5,6,6)
# print(t[0:3])

# Check if item exists 
# a = ("ap",'sd','ad')
# if "ap" in a:
#     print(True)

# Update tuples
# Tuples are unchangable, meaning that you cannot change ,
# add, or remove items once the tuple is created.

# Converting tuple to list and after changing values ,converting back to tuple()
# x =("apple","banna","cherry")
# y = list(x)
# add element 
# y.append("Cucumber")
# change element by using it's index
# y[1]= "kiwi"
# x = tuple(y)
# print(x) 

# Revision
# x = ('2','3','4')
# new = list(x)
# new.append("Sosages")
# x = tuple(new)
# print(x)


print("hello, world")








