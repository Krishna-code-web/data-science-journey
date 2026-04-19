# 1. Robust Division with Multiple Exceptions 

# Question: Write a function divide_numbers that takes two inputs from a user. Handle the following scenarios: 
# ValueError: If the user enters something other than a number.
# ZeroDivisionError: If the user attempts to divide by zero.
# General Exception: Catch any other unexpected errors using a broad exception.
# Cleanup: Use a finally block to print "Calculation attempt finished" regardless of the outcome.

# def divide_numbers():
#     try:
#         num1 = int(input("Enter first Number : "))
#         num2 = int(input("Enter second Number : "))
#         result = num1/num2
#     except ValueError as v:
#         print(f"Oops! you entered something different! {v}")
#     except ZeroDivisionError as z:
#         print(f"Oops! you try to divide by 0! {z}")
#     except Exception as e:
#         print(f"Something went wrong! {e}")
#     else:
#         print(f"The result is: {result}")
#     finally:
#         print("Calculation attempt finished!")

# divide_numbers()

# 2. Custom Exception for Range Validation
# Question: Create a custom exception class called AgeLimitError. Write a program that asks a user for their age and: 
# Raises AgeLimitError if the age is less than 0 or greater than 120, with a message "Invalid age range".
# Handles ValueError if the input is not an integer.
# Use the else block to print "Age accepted" if no exceptions occur.

# class AgeLimitError(Exception):
#     """Custom exception for age range validation."""
#     pass

# def check_age():
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0 or age > 120:
#             raise AgeLimitError("Age must be between 0 and 120.")
#     except ValueError:
#         print("Error: Input must be a whole number.")
#     except AgeLimitError as e:
#         print(f"Validation Error: {e}")
#     else:
#         print(f"Age {age} is accepted.")

# check_age()

