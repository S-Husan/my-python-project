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
#                                                   SLIDES FORM 90-151
# ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Python PIP (PIP insatll package)
# import camelcase
# # c= camelcase.CamelCase()
# # txt = "i am groot, and i am a groot"
# # print(c.hump(txt))  # <=== The .hump() method looks at your text and capitalizes the first letter of every word.



try:
    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: That wasn't a valid number!")
else:
    print(f"Success! The result is {result}")
finally:
    print("Execution complete.")