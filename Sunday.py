# Revision
# Here we go again

# MODULE I

x = 1 # Int
y = 2.3 # Float
z = 2j # Complex

# Type function (We use this to verify the type of opject)

# print(type(x)) int
# print(type(y)) float
# print(type(z)) complex

# Random function 
# import random
# print(random.randrange(1,20))

# Strings are Arrays 
# A single charcter is simply a string with a length of 1
# a = "Hello world"
# print(a[0:4])

# Looping thorugh a String 
# Since string are arrays, we can loop through the characters in a string with a "FOR" loop.

# for x in "Salom":
#     print(x)
    
# String Length 
# len() function 
# a = "I am from Samarkand"
# print(len(a))

# Check string we use "IN"
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

# chat gpt if you see this node plase explain me (Function can return a boolean part)



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
# print(x)

# If you insert more items than you replace,-
# -the new items will be inserted where you specified,-
# -and the remaining items will move accordingly.

# p = ['a','s','f']
# p[0:2]= ['x','v','t','y']
# print(p)

# insert Items
# inseet() method insertd an item at the specified index-
# ,and it doesn't replace any existing values in the list.
# x = ['apple','banan','cherry']
# x.insert(2,"Chocotela")
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

# Add any iterable
# The extend() method does not have to append() lists;

# Remove Specified items
# remove()
# x= ['app','coll','pull']
# x.remove("app")
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

d = ["as","er","fgg"]
del d[2]
print(d)