# Syntax Error 
# print("Hello World"
      
# Indentation Error 
# def func():
# print("Hello!")

# These errors cannot be handled, but exceptions can be handled.

# Exceptions

# Exception 	Triggered When...
# ValueError	A function receives an argument of the right type but inappropriate value (e.g., int("abc")).
# FileNotFoundError	An attempt to open a file that does not exist fails.
# TypeError	An operation is applied to an object of an inappropriate type (e.g., 5 + "10").
# IndexError	An attempt is made to access an index that is out of range for a list or tuple.

# print("Start")
# print(10/0) # ZeroDivisionError
# print("End") # This line will never run

# Example

# print("Start")
# try:
#     # Write only that code which is expected to get an exception
#     print(10/0)
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")
# else:
#     print("Division Successful!")
# print("End")

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print(f"Your age is {age}.")
# except ValueError as e:
#     print(f"Invalid input: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
