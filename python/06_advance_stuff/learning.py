# 1) Decorator

# def my_decorator(func):
#     def wrapper():
#         print('Something before the function runs!')
#         func()
#         print('Something after the function runs!')
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print('Hello!', name)

# say_hello('krishna')

# For making the decorator with Arguments it is tough for this we
# will move towards our next advance stuff *args , **kwargs.

# 2) Args and Kwargs

# And the *args becomes a tuple and **kwargs becomes a
# dictionary

# The use case is great
# You don’t need to know how many inputs you'll get
# Helps in building flexible functions, decorators, APIs, and
# more

# def fun(*args, **kwargs):
#     print('Args:', args)
#     print('Kwargs:', kwargs)

# fun(1,2,3,name='Arin',age=21)

# 3) List, Dictionary and set comphrehension, Lambda functions

# labels = ["Even" if x%2==0 else "Odd" for x in range(5)]
# print(labels)

# evens = {x: x*x for x in range(10) if x%2==0}
# print(evens)

# unique_even_squares = {x*x for x in range(10) if x%2==0}
# print(unique_even_squares)

# A lambda function is an anonymous, inline function defined using
# the lambda keyword

# square = lambda x: x**2
# print(square(4))

# check_even = lambda x:"Even" if x%2==0 else "Odd"
# print(check_even(6))

# Map, filter and zip

# Map is used for applying a function to multiple items.
# Takes a list (or any sequence
# Applies the same function to every item in that lis
# Gives you back a new list (in Python 3, it gives a map object
# which you can convert to a list)

# numbers = [1,2,3,4]
# doubled = map(lambda x:x*2, numbers)
# print(list(doubled))

# Filter as the name suggest is used to filter out the stuff.
# Takes a list (or other sequence
# Checks each item using a function (a test
# Keeps only the items that pass the test (i.e., return True)

# def check(num):
#     if num%2==0:
#         return True
#     return False

# numbers = [1,2,3,4,5]
# evens = filter(lambda x:x%2==0, numbers)
# print(list(evens))


# Modules and Packages

# Module is just a single file containing code and we can use this
# file code in other file
# A single Python file (.py)
# Contains functions, variables, or classes
# Used to organize and reuse code
# Python comes with lots of ready-to-use modules like
# math (for math operations)
# random (for generating random numbers)
# datetime (for date and time)

# import math  # module
# print(math.sqrt(25))

# A package is a folder that contains one or more modules (Python
# files). It may also contain sub-packages (like matplotlib.pyplot)
# and you just have to use from and import keywords to use these
# things. You understood how these things work.
# There are third party packages as well like numpy, pandas,
# matplotlib etc. and we have to install all of these.