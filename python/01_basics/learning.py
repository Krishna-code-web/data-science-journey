# # Comments are something that is ignored by python interpreter 

# # 1) # is single line comment and multiline comment is not available in python 
# '''but using docstring multiline comments 
# can be used!'''

# name = 'krishna' # Variable
# age = 21  # Variable

# # Data Types

# # 1) Numbers
# a = 10
# b = 20.5
# c = 10 + 20j
# print(a, b, c)

# # 2) Strings
# name = 'krishna'
# print(name)

# # 3) Boolean
# ans = True | False
# print(ans)

# # Strings and Type Conversion

# a = 'A'
# print(ord(a))
# b = 128522
# print(chr(b))

# string = 'Hello'
# print(string[0])
# print(string[-1])

# # String slicing
# print(string[1:4:1])

# # Type conversion
# a = 10 
# print(a/2)

# b = 70
# print(chr(b))

# Input and Output 

# name = input("Enter your name : ")
# print(f"Hi! {name}")

# Accept numbers from a user
# numbers = int(input("Enter any number"))
# print(f"You entered : {numbers}")

# Accept age from the user and print it.
# age = int(input("Enter your age : "))
# print(f"Your age is {age}")

# Operators

# Arithmetic +, -, *, /, //, %, **
# Assignment =, +=, -=, *=, /=, //=, %=, **=
# Comparison ==, !=, >, <, >=, <=
# Logical and, or, not

# print(126 > 130)  # False
# print((456==456) != (235==236)) # True
# print(12 < 10 or 45==56 or 69>70 or 15!=13) # True
# print(True and bool(0)) # False

# Conditional Statements

# Conditional statements in Python allow decision-making by
# executing different blocks of code based on conditions
# Decision making can be understood with an example 

# eg - you will receive a number from the user if the number is 
# greater than 10 you will do task A and lower than 10 you 
# will do task B.

# Loops

# for loop

# for i in range(1, 6):
#     print(i)

# a = "Nature"

# for i in range(len(a)):
#     print(a[i])

# for char in a:
#     print(char)

# while loop

# ans = True
# i = 1
# while ans:
#     print(i, end=' ')
#     i += 1
#     if i==6:
#         ans = False

# Functions

# def greet():
#     print("Hello EveryOne!")

# greet()

# # This is positional Argument!
# def greet(name): # name is a parameter
#     print(f'Hello {name}')

# greet('krishna') # krishna is an argument

# Types of arguments

# 1) Positional Arguments
# def add(a,b):
#     return a+b

# print(add(3,5))

# # 2) Keyword Arguments 
# def introduce(name, age):
#     print(f"I am {name} and I am {age} years old!")

# introduce(age=21, name='krishna')

# # 3) Default Arguments
# def greet(name='krishna'):
#     print(f'Hello, {name}!')

# greet()
# greet('Pathan')


    

