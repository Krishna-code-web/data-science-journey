# Lets be clear this python notes are not for the DSA this will
# cover all the in-build data structures.

# 1) List 

# fruits = ['apple', 'banana', 'cherry']
# print(fruits)

# numbers = [10, 20, 30, 40]
# numbers[1] = 99
# print(numbers)

# List traversing 

# for i in numbers:
#     print(i, end=' ')

# List methods

# numbers = [5, 2, 9, 1, 5, 6] # Initial List
# print(numbers) # Print list

# numbers.append(10) # Add 10 to the end
# print(numbers) 
# numbers.insert(2, 15) # Inserts 15 at index 2
# print(numbers) 
# numbers.extend([20, 25, 30]) # Adds multiple elements at the end
# print(numbers) 
# numbers.remove(5) # Removes the first occurence of 5
# print(numbers) 
# popped_item = numbers.pop(3) # Removes and stores the element at index 3
# print(numbers) 
# index = numbers.index(6) # finds the index of 6
# print(index) 
# count_5 = numbers.count(5) # Counts occurences of 5
# print(count_5) 
# numbers.sort() # Sorts the list in the ascending order
# print(numbers) 
# numbers.reverse() # Reverse the list order
# print(numbers) 
# new_numbers = numbers.copy() # Creates a copy of the list
# print(new_numbers) 
# numbers.clear() # Removes all elements from the list
# print(numbers) 

# 2) Tuple

# t = (5,2,9,1,5,6) # Initial tuple
# print(t)

# index = t.index(9) # finds the index of first occurenec of 9
# print(index)
# count_5 = t.count(5) # counts occurences of 5
# print(count_5)

# 3) Set 

# s = {1,2,3}
# print(s)

# s.add(4) # Adds an element to the set
# print(s)
# s.remove(2) # Removes 2 (Raises an error if not found)
# print(s)
# s.discard(5) # Removes 5 (No error if not found)
# print(s)
# popped_element = s.pop() # Removes a random element
# print(s)
# s.clear() # Removes all elements
# print(s)

# A = {1,2,3}
# B = {3,4,5}

# union_set = A.union(B)
# print(union_set)
# intersection_set = A.intersection(B)
# print(intersection_set)
# differenece_set = A.difference(B)
# print(differenece_set)
# symmetric_diff = A.symmetric_difference(B)
# print(symmetric_diff)

# 4) Dictionary

# student = {
#     "name": "John", 
#     "age": 28
# }
# print(student["name"]) # Output: John

# numbers = {1: 10, 2:20, 3:30, 4:40}

# for i in numbers:
#     print(i, ":", numbers[i])

# help(dict)







