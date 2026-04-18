# Conditional Questions

# Q1. Accept two numbers and print the greatest between them.

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# if num1 > num2:
#     print(f'{num1} is greatest!')
# else:
#     print(f'{num2} is greatest!')

# Q2. Accept the gender from the user as char and print the 
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)

# gender = input("Enter your Gender (M or F) : ")

# if gender == 'M' or gender == 'm':
#     print(f'Good Morning Sir')
# else: 
#     print(f'Good Morning Mam')

# Q3. Accept an integer and check whether it is an even number 
# or odd.

# number = int(input("Enter any integer : "))
# if number%2==0:
#     print(f'{number} is Even!')
# else:
#     print(f'{number} is Odd!')

# Q4. Accept name and age from the user. Check if the user is a 
# valid voter or not.
# Ex- “hello shery you are a valid voter”

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# if age > 18:
#     print(f'hello {name} you are a valid voter!')
# else:
#     print(f'hello {name} you are not a valid voter!')

# Q5. Accept a year and check if it a leap year or not (google to 
# find out what is a leap year)

# year = int(input("Enter the year : "))

# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(f'{year} is a leap year!')
# else:
#     print(f'{year} is not a leap year!')

# Q6. For understanding solve this question
# take the input of temperature in celsius
# Below 0°C → "Freezing Cold
# 0°C to 10°C → "Very Cold
# 10°C to 20°C → "Cold
# 20°C to 30°C → "Pleasant
# 30°C to 40°C → "Hot
# Above 40°C → "Very Hot "

# temp = int(input("Enter the temperature in Celsius : "))

# if temp < 0:
#     print("Freezing Cold!")
# elif temp < 10:
#     print("Very Cold!")
# elif temp < 20:
#     print("Cold!")
# elif temp < 30:
#     print("Pleasant")
# elif temp < 40:
#     print("Hot")
# else: 
#     print("Very Hot")

# For Loop questions

# Q1 Accept an integer and Print hello world n times

# n = int(input("Enter a number : "))

# for i in range(n):
#     print('Hello World!')

# Q2 Print natural number up to n

# n = int(input("Enter a number : "))

# for i in range(1, n+1):
#     print(i, end="")

# Q3. Reverse for loop. Print n to 1

# n = int(input("Enter a number : "))

# for i in range(n, 0, -1):
#     print(i, end="")

# Q4. Take a number as input and print its table

# number = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(f'{number} * {i} = {number*i}')

# Q5. Sum up to n terms

# n = int(input("Enter a number : "))
# sum = 0

# for i in range(1, n+1):
#     sum += i
# print(f'Sum is {sum}')

# Q6. Factorial of a number

# n = int(input("Enter a number : "))
# fact = 1

# for i in range(1,n+1):
#     fact *= i
# print(f'Factorial of {n} is {fact}')

# Q7. Print the sum of all even & odd numbers in a range
# separately.

# n = int(input("Enter a number : "))
# even = 0
# odd = 0

# for i in range(1, n+1):
#     if i%2==0:
#         even += i
#     else:
#         odd += i
# print(f"Even Number sum is {even}")
# print(f"Odd Number sum is {odd}")

# Q8. Print all the factors of a number

# n = int(input("Enter a number : "))

# for i in range(1, n+1):
#     if n%i==0:
#         print(i, end=" ")

# Q9. Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself

# Ex - 6 = 1, 2, 3 = 6

# n = int(input("Enter a number : "))
# sum = 0

# for i in range(1, n):
#     if n%i==0:
#         sum += i

# if sum == n:
#     print("Perfect Number!")
# else:
#     print("Not a Perfect Number!")


# Q10. Reverse a string without using in build functions.

# string = input("Enter any String : ")
# reverse = ''

# for i in string:
#     reverse = i + reverse
# print(reverse)
    
# string = input("Enter any String : ")
# print(string[::-1])

# Q11. Check string is Pallindrome or not

# string = input("Enter any String : ")
# reverse = string[::-1]

# if string == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Q12. Count all letters, digits, and special symbols from a given
# string

# Given: str1 = "P@#yn26at^&i5ve"

# Expected Outcome:
# Total counts of chars, digits, and symbols

# Chars = 8
# Digits = 3
# Symbol = 4

# str1 = input("Enter a string : ")
# chars = 0
# digits = 0
# symbols = 0

# for i in str1:
#     if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
#         chars += 1
#     elif (i >= '0' and i <= '9'):
#         digits += 1
#     else:
#         symbols += 1
# print(f'Chars: {chars} \nDigits: {digits} \nSymbols: {symbols} \n ')


# While Loop Questions 

# Q1. Separate each digit of a number and print it on the new line

# number = int(input("Enter the Number : "))

# while number != 0:
#     print(number%10)
#     number //= 10

# Q2. Accept a number and print its reverse

# number = int(input("Enter the Number : "))
# reverse = 0

# while number != 0:
#     reverse = reverse*10 + number%10
#     number //= 10

# print(f'Reverse is : {reverse}')

# Q3. Accept a number and check if it is a pallindromic number (If
# number and its reverse are equal

# number = int(input("Enter the Number : "))
# n = number
# reverse = 0

# while number != 0:
#     reverse = reverse*10 + number%10
#     number //= 10

# if reverse == n:
#     print(f'{n} is a Palindrome Number!')
# else:
#     print(f'{n} is not a Palindrome Number!')

# Q4. Create a random number guessing game with python.
# import random
# random_number = random.randint(1, 100)
# n = 0
# ans = True

# while ans:
#     number = int(input("Guess the number : "))
#     n += 1

#     if number == random_number:
#         print(f"Number is guessed in {n} attempts!")
#         ans = False
#     elif number < random_number:
#         print("Too Low!")
#     else:
#         print("Too High!")






