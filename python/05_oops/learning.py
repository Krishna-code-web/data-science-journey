# There are three programming paradigms or methods

# 1) Imperative Approach

# a = 12 
# b = 12
# print(a+b)

# 2) Functional Approach

# def addition(a, b):
#     return a+b

# print(addition(12,12))
# print(addition(45,45))

# 3) Object-Oriented Approach

# class Addition:
#     def __init__(self, a, b):
#         print(a+b)

# obj = Addition(12,12)

# Classes in OOPS

# class Animal:                      #Class
#     species = 'Dog'                #Attribute

#     def make_sound(self):          #Method
#         print('Bark!')

# # Accessing Attributes and Method directly.

# print(Animal().species)
# Animal().make_sound()


# Objects in OOPS

# class Fruit:
#     name = 'Apple'

# # Creating an object
# f = Fruit()
# print(f.name)

# Constructor

# class Student:
#     def __init__(self, name):
#         self.name = name # Instance attribute

# # Creating an object with a value
# s = Student('Krishna')
# print(s.name)

# Attributes and Methods 

# Types of Attribute 

# class Car:
#     wheels = 4                  # Class attribute

#     def __init__(self, color):
#         self.color = color      # Instance attribute

# Types of methods

# 1) Instance Method 

# class MyClass:
#     def instance_method(self):
#         print("This is an instance method!")

#     @classmethod
#     def class_method(cls):
#         print("This is a class method!")

#     @staticmethod
#     def static_method():
#         print("This is a static method!")

# obj1 = MyClass()
# obj1.instance_method()
# MyClass().instance_method()
# MyClass().class_method()
# MyClass().static_method()


# Inheritance

# Inheritance allows a class (child class) to inherit properties and
# behaviors (attributes and methods) from another class (parent
# class)

# class Parent:
#     def speak(self):
#         print("I can speak!")
    
# class Child(Parent):   # Inherits Parent Class
#     pass

# obj = Child()
# obj.speak()

# Constructor in Inheritance

# Lets say you have created a parent class with a constructor
# function inside it and then this class is inherited by another class
# then the constructor function of parent class will work for the
# child class as well.

# class Parent:
#     def __init__(self, name):
#         self.name = name

# class Child(Parent):
#     def display(self):
#         print(f'My name is {self.name}')

# obj = Child('krishna')
# obj.display()

# Now lets say you need a new parameter in your child class you
# have to create a constructor function for your child class but the
# parameters that can be initialized in the parent class will be
# initialized using the super() function. Super function will target the
# parent class.

# class Parent:
#     def __init__(self, name):
#         self.name = name

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
    
#     def display(self):
#         print(f'My name is {self.name}, I am {self.age} years old!')

# obj = Child('krishna', 21)
# obj.display()

# Types of Inheritance

# 1) Single Inheritance 

# 2) Multiple Inheritance 

# class Father:
#     def skills(self):
#         print('Coding')

# class Mother:
#     def skills(self):
#         print('Cooking')

# class Child(Father, Mother):
#     def show(self):
#         print('I have multiple skills')

# obj = Child()
# obj.show()
# obj.skills()

# 3) Multi-level Inheritance

# class Father:
#     def skills(self):
#         print('Coding')

# class Mother(Father):
#     def skill(self):
#         print('Cooking')

# class Child(Mother):
#     def show(self):
#         print('I have multiple skills')

# obj = Child()
# obj.show()
# obj.skill()
# obj.skills()


# Polymorphism

# The word means "many forms" — and in programming, it
# allows the same interface or method name to behave differently
# depending on the object or context.

# 1) Method Overloading  # Not supported in python

# Polymorphism can be achieved in python in two ways well if we
# talk about compile time languages there are 3 ways but python
# does not support Method overloading

# Method overloading means having same name methods inside a
# class but parameters will be different but in python the latest
# definition will overwrite the previous one

# 2) Method Overriding

# This is where a child class overrides a method of the parent
# class, and Python decides at runtime which method to call,
# based on the object type.

# class Animal:
#     def sound(self):
#         print(f'Animal makes a sound!')
    
# class Dog(Animal):
#     def sound(self):
#         print(f'Dog Barks')

# obj1 = Animal()
# obj1.sound()
# obj2 = Dog()
# obj2.sound()

# 3) Duck Typing 

# Python program to demonstrate
# duck typing

# Python follows the philosophy: 
# “If it walks like a duck and quacks like a duck, it must be a
# duck.

# class Bird:
#     def fly(self):
#         print("fly with wings")

# class Airplane:
#     def fly(self):
#         print("fly with fuel")

# class Fish:
#     def swim(self):
#         print("fish swim in sea")

# # Attributes having same name are
# # considered as duck typing
# for obj in Bird(), Airplane():
#     obj.fly()


# Encapsulation

# Encapsulation means putting data (variables) and code (functions)
# together in one place — inside a class
# It also means hiding the internal details of how things work, and
# only showing what is needed

# Access modifiers in python

# 1) Public attributes and methods 

# Till now every attribute and methods we have created are
# public means the inherited classes and objects can access
# them no matter what

# 2) Protected attributes ansd methods

# python protected members are created using a single
# underscore but it still can be accessed from outside the
# class so you might wonder whats the point of using them
# Python doesn’t enforce protected access like other
# languages (e.g., Java or C++). But it uses a naming
# convention to tell developers

# 3) Private attributes and methods

# A private variable or method means
# It cannot be accessed from outside the class — only from
# inside the class where it is defined
# In Python, we use two underscores (__) before the name to
# make it private.

# class Demo:
#     def __init__(self):
#         self.name = 'krishna'    # public
#         self._age = 21           # protected   
#         self.__salary = 50000    # private
    
#     def show(self):
#         print("Inside the class:")
#         print("Public:", self.name)
#         print("Protected:", self._age)
#         print("Private:", self.__salary)

# obj = Demo()
# obj.show()


# Abstraction

# Abstraction does not exist in python but we can achieve it using a
# library we will see what is a library later.
# Abstraction is used to simplifying complex systems by focusing
# on essential features and hiding unnecessary details
# It is used to define a common interface for different subclasses.

# Abstract methods and classes

# Abstract classes are classes that contains one or more abstract
# methods
# A method that is defined but not implemented in the abstract
# class. subclasses must provide the implementation.

# from abc import ABC, abstractmethod

# class Animal(ABC):     # abstract class
#     @abstractmethod
#     def make_sound(self):   # abstract method
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print(f'Dog says Woof!')

# class Cat(Animal):
#     def make_sound(self):
#         print(f'Cat says Meow!')

# obj1 = Dog()
# obj2 = Cat()
# obj1.make_sound()
# obj2.make_sound()


# Dunder Methods

# Dunder methods are special methods in Python that start and
# end with double underscores, like __init__, __str__, __add__, etc
# They automatically get called when you perform certain actions
# on an object
# They help you
# Customize behavior of your clas
# Make your class objects behave like built-in data types (like
# strings, lists, etc.

# class Person:
#     # Both are dunder methods 
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f'My name is {self.name}'
    
# obj = Person('krishna')
# print(obj)






