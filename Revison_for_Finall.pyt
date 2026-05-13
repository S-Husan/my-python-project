# print ("Here we go again")
# 

# ///////
# LOOPING the string
# a = "HEllO wolrd"
# for i in a:
#     print(i)


# Modefy String
# a= " SALOM, dunyo"
# b= "salom"

# # a.lower()
# b.upper()
# # a.strip()

# print(a.strip())
# print(b.replace("s","S"))



# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#                                             SLIDES FORM 90-151
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Python PIP (PIP insatll package)
# import camelcase
# c= camelcase.CamelCase()
# txt = "i am groot, and i am a groot"
# print(c.hump(txt))  # <=== The .hump() method looks at your text and capitalizes the first letter of every word.



# try:
#     number = int(input("Enter a number to divide 10 by: "))
#     result = 10 / number
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")
# except ValueError:
#     print("Error: That wasn't a valid number!")
# else:
#     print(f"Success! The result is {result}")
# finally:
#     print("Execution complete.")
    
# try:
#     number= int(input("Enter a number: "))
#     print("==============")
#     result= 10/ number
#     print("==============")
#     print(f"Result is {result}")
#     print("==============")
# except ZeroDivisionError:
#     print("You can't devide by 0")
#     print("==============")
# except ValueError:
#     print("That is not a valid number")
#     print("==============")
# else:
#     print("No erros identified")
#     print("==============")
# finally:
#     print("The task is done, no metter succed or not")
    
    
    
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#                                       String formating
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
    
# food= 'Burger'
# price = 49
# a= 'The price for {} is {:.2f} dollars'
# print(a.format(food,price))

# Index number
# food1= 'Colla'
# price1 = 2
# discount= 1
# a1= 'The price for {0} is ${1:.2f}, but for this {0} u can get a discount ${3:.2f} !'
# print(a1.format(food1,price1,food1,discount))


# NAMED INDEXES

# food1= 'Colla'
# price1 = 2
# discount= 1
# a1= 'The price for {0} is ${1:.2f}, but for this {0} u can get a discount ${3:.2f} !'
# print(a1.format(food1,price1,food1,discount))

# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#                                       File handling
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
    
#Read data from files
# Write data to files
# Manipulate file contents
# Work with different file formats


# File modules 
# r (Read): Opens for reading. Fails if file is missing. (Default)
# a (Append): Adds text to the end. Creates file if missing.
# w (Write): Overwrites content. Creates file if missing.
# x (Create): Creates new file. Fails if file already exists.
# t (Text): For standard text files. (Default)
# b (Binary): For non-text files (images, PDFs).
# + (Update): Enables both reading and writing simultaneously.

#===============================||
# r	Read	Opens	Error       ||
# w	Write	Overwrites	Creates ||
# a	Append	Adds to end	Creates ||
# x	Create	Error	Creates     ||
#===============================||


# . Combinations:
# . 'rb' - Read binary
# . 'wb' - Write binary
# . 'ab' - Append binary
# . 'r+' - Read and write (no truncate)
# . 'w+' - Read and write (truncate)
# . 'a+' - Read and append
# . 'rb+' - Read and write binary

# Pritice
# f= open('test.txt')
# print(f.read())

# f.close()


# f.close() happens here automatically!
# with open('test.txt', 'r') as file:
#     print(f"File name: {file.name}")
#     print(f"File mode: {file.mode}")
#     print(f"Is the file closed? {file.closed}")
#     print(f"File encoding: {file.encoding}")
    
# file.close()

# with open("test.txt","r") as f:
#     print(f'File name: {file.encoding  }')
    
    
# Reading a file


# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
#                                SLIDES FORM 90-151 Last preperation 
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# PIP prefereed install package 

# Numpy numerical python 

# with open('test.txt', 'r') as file:
#     print(f"File name: {file.name}")
#     print(f"File mode: {file.mode}")
#     print(f"Is the file closed? {file.closed}")
#     print(f"File encoding: {file.encoding}")
    
# file.close()


# 

# try:
#     # risky code
#     pass
# except SomeError:
#     # runs if error happens
#     pass
# else:
#     # runs if NO error happens
#     pass
# finally:
#     print('The excectuion is done')

try:
    user_name = input("Enter your name: ")
    
    if user_name.lower() != "husan":
        # We manually raise an error if the name is wrong
        raise ValueError("Unauthorized User")
        
except ValueError:
    print("You are not an Admin")

else:
    # This runs ONLY if no ValueError was raised
    print("You are allowed to enter,", user_name)

finally:
    print("The authentication has completed")
    
try:
    EnterAge= int(input("Enter your age: "))
    if 18 > EnterAge:
        print("You are not allowed to watch this Web")
        raise ValueError("Unauthorized User")
except ValueError:
    print('You are still child')
else:
    print("Your age is valid u can visit  webosite")
finally :

    print("The authorization has complited withoun and error")
    
