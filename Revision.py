# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# op = input("Enter operation (+ - * /): ")

# if op == "+":
#     print("Result:", a + b)
# elif op == "-":
#     print("Result:", a - b)
# elif op == "*":
#     print("Result:", a * b)
# elif op == "/":
#     if b == 0:
#         print("Error: Division by zero")
#     else:
#         print("Result:", a / b)
# else:
#     print("Invalid operation")


# print(type('a'))
# print(int(1))
# print(233)


# import random 
# print(random.randrange(2,10))

# print("Hello")


# print("Hi i am mentally unstable, becasue iam learning Java at university and Python with ML")
# print("I wanted to be financially stable, but now I am mentally unstable.😭😭")




# /////////////////////////////////////////////////////////////////////////////////


# # home task
# # factorial counter

# def factorial(number):
#     factorial =1
#     if(number < 0):    print("No factorial") 
#     elif(number == 0): print(1)
#     else:
#         for i in range(number, 0, -1):
#             factorial *= i
#         print(factorial)
            
# factorial(2)

# /.///////////////////////////////////////////////////////////////////////////////
# Grading machine myde by me
# Simple grading system using functions


# def calculate_grades():

#     math = int(input("Enter Math score: "))
#     english = int(input("Enter English score: "))
#     python = int(input("Enter Python score: "))

#     total = math + english + python
#     average = total / 3

#     if average >= 90:
#         mark = "+A"
#     elif average >= 80:
#         mark = "A"
#     elif average >= 70:
#         mark = "B"
#     elif average >= 60:
#         mark = "C"
#     elif average >= 50:
#         mark = "D"
#     else:
#         mark = "F"
#     print("\nTotal:", total)
#     print("Average:", average)
#     print("Final Grade:", mark)
    
# calculate_grades()



# ///////////////////////////////////////////////////////////////////////////////////////
# New topic
# Fibonocci sequence 


# n = int(input("Enter the number:"))
# n1 ,n2 = 0,1
# count = 0
# if n<= 0:
#     print('Enter positive number')
# elif n ==1:
#     print("It's",n,":")
#     print(n1)
# else:
#     print("fibanocci sequence is:")
#     while count < n:
#         print(n1)
#         n3 = n1+n2
#         n1 = n2
#         n2 = n3
#         count = count + 1 




# /////////////////////////////////////////////////////////////////////////////////
# Recursion (function calls itself direcly or inderectly again and again until problem solves)

# def f is name(parameter)

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n*f(n-1)
# n = int(input("Enter a number:"))
# if n < 0:
#     print("Enter Positivr")
# else:
#     r = f(n)
#     print(r)

# print("Men tibbiyot ")

# /////////////////////////////////////////////
# Revision at home
