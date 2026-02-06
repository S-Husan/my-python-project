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


class person:
    def __init__(self,name,age):
        self.name = name
        self.age= age     


p1= person("name:Galety","age 52",)
p2= person("name:Rafi","age 41")


p1.name = "Mohammed"

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

print("---------------------------------------------------")

# Delite object properties
class person:
    def __init__(self,money,car,house):
        self.money = money
        self.car= car      
        self.house=house

zafar = person("100$", "Car","House")
md = person("500$", "laceti","big house")
print("Before-Zafar properties")
print(zafar.money, "|""\t\t", zafar.car, "|""\t\t",zafar.house)

del zafar.money


print("---------------------------------------------------")
print("After-Zafar properties")
print("none" ,"|""\t\t",zafar.car,"|" "\t\t",zafar.house)
print(zafar)


