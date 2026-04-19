# List Questions

# Q1) Print positive and negative elements of an List

# n = int(input("Enter the size of the list : "))
# l = []

# for i in range(n):
#     element = int(input("Enter any integer : "))
#     l.append(element)

# positive = []
# negative = []
# for i in l:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)
    
# print("Positive Numbers are : ", positive)
# print("Negative Numbers are : ", negative)

# Q2) Mean of List elements

# n = int(input("Enter the size of the list : "))
# l = []

# for i in range(n):
#     element = int(input("Enter any integer : "))
#     l.append(element)

# sum = 0
# for i in l:
#     sum += i
# print("Mean of all elements of the list is : ", sum/len(l))

# Q3) Find the greatest element and print its index too.

# n = int(input("Enter the size of the list : "))
# l = []

# for i in range(n):
#     element = int(input("Enter any integer : "))
#     l.append(element)

# greatest = l[0]
# for i in l:
#     if i > greatest:
#         greatest = i
# print(f"Greatest Element in the list is : ", greatest)

# Q4) Find the second greatest element

# Works only for positive element 
# n = int(input("Enter the size of the list : "))
# l = []

# for i in range(n):
#     element = int(input("Enter any positive integer : "))
#     l.append(element)

# greatest = -1
# second_greatest = -1
# for i in l:
#     if i > greatest:
#         second_greatest = greatest
#         greatest = i
#     elif i > second_greatest:
#         second_greatest = i
# print(f"Second Greatest Element in the list is : ", second_greatest)

# Q5) Check if List is sorted or not.

# n = int(input("Enter the size of the list : "))
# l = []

# for i in range(n):
#     element = int(input("Enter any  integer : "))
#     l.append(element)

# ans = True
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         ans = False
#         break

# if ans == True:
#     print(f'List is Sorted!')
# else:
#     print(f'List is not Sorted!')

# Dictionary Questions

# Q1) Write a Python script to merge two Python dictionaries

# dict1 = {
#     "name": 'krishna',
#     "age": 21
# }

# dict2 = {
#     "name": 'krishna',
#     "programme": "BTech", 
#     "branch": "CSE", 
#     "specialization": "AI, ML and DL"
# }

# merged_dict = dict()

# for key in dict1:
#     merged_dict[key] = dict1[key]

# for key in dict2:
#     merged_dict[key] = dict2[key]

# for key in merged_dict:
#     print(f'{key} : {merged_dict[key]}')

# 2) merged_dict = {**dict1, **dict2}
# 3) merged_dict = dict1 | dict2

# Q2) Write a Python program to sum all the values in a dictionary.

# dict1 = {
#     '1': 10,
#     '2': 20,
#     '3': 30,
#     '4': 40,
#     '5': 50
# }

# sum = 0
# for i in dict1:
#     sum += dict1[i]
# print(f'Sum of all the values of dictionary is : {sum}')

# Q3) Count the frequency of each element

# my_dict = {
#     "a": 1,
#     "b": 1,
#     "c": 2,
#     "d": 1
# }

# freq = {}

# for i in my_dict:
#     if my_dict[i] in freq:
#         freq[my_dict[i]] = freq[my_dict[i]] + 1
#     else:
#         freq[my_dict[i]] = 1

# for i in freq:
#     print(f'{i} : {freq[i]}')

# Q4) Write a Python program to combine two dictionary by adding values for common keys.

# dict1 = {
#     'first': 10,
#     'second': 20,
#     'third': 30
# }

# dict2 = {
#     'first': 10,
#     'second': 20,
#     'fourth': 40
# }

# dict3 = {}

# for i in dict1:
#     dict3[i] = dict1[i]

# for i in dict2:
#     if i in dict3:
#         dict3[i] = dict3[i] + dict2[i]
#     else:
#         dict3[i] = dict2[i]

# for i in dict3:
#     print(f'{i} : {dict3[i]}')
