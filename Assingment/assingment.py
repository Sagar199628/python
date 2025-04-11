

# Introduction to Python Theory:
# Lab

# Q.1
# print("Hello, World!")
# print("SAGAR KHODIYAR")

# Q.2
# This program calculates the area of a rectangle
# rectangle_width = 5.0
# rectangle_height = 3.0

# Calculate the area
# area =(rectangle_width * rectangle_height)

# Print the result
# print(f"The area of the rectangle is: {area}")

# Q.3
# Demonstrating Different Data Types in Python

# # Integer
# age = 25
# print("Integer (age):", age)
#
# # Float
# height = 5.9
# print("Float (height):", height)
#
# # String
# name = "Sagar"
# print("String (name):", name)
#
# # List (a collection of items)
# fruits = ["apple", "banana", "cherry"]
# print("List (fruits):", fruits)
#
# # Tuple (similar to list but immutable)
# coordinates = (10.0, 20.0)
# print("Tuple (coordinates):", coordinates)
#
# # Dictionary (key-value pairs)
# person = {
#     "name": "Sagar",
#     "age": 25,
#     "height": 5.9
# }
# print("Dictionary (person):", person)
#
# # Boolean
# is_student = True
# print("Boolean (is_student):", is_student)
#
# # Demonstrating some operations
# # Update variable
# age = 1
# print("Updated age:", age)
#
# # Adding an item to a list
# fruits.append("orange")
# print("Updated List (fruits):", fruits)
#
# # Accessing dictionary values
# print("Person's Name:", person["name"])

# Q.3.1
# Python code structure is essential for writing clear, maintainable, and effective code.
# Understanding the basic elements of Python's structure helps you develop well-organized programs

# 1. Indentation
# Python uses indentation to define the scope of loops, functions, classes, and conditionals.
# Consistent indentation (usually 4 spaces) is crucial as it affects how the code is interpreted.

# def my_function():
    # print("Hello, World!")  # This belongs to my_function
# my_function()

# 2. Comments
# Comments are annotations in the code to explain what certain parts do.
# They start with a (#) for single-line comments or three quotes for multi-line comments.

# This is a single line comment.

# "
# This is a
# multi-line comment
# "

# 3.3. Modules and Imports
# Code can be organized into modules (separate .py files) and packages (directories containing modules).
# We can import these modules using the import statement.

# import math  # Importing a standard library module
# from my_module import my_function  # Importing a specific function

# 3.4. Variables and Data Types
# Variables in Python are created by assignment.
# Python supports several data types, including integers, floats, strings, lists, tuples, dictionaries, and sets.

# x = 10                     # Integer
# y = 3.14                   # Float
# name = "Sagar"             # String
# numbers = [1, 2, 3, 4]     # List
# coordinates = (10, 20)     # Tuple
# info = {'name': 'Sagar'}    # Dictionary

# 3.5.# Prompt the user for input
# user_input = input("Please enter something: ")

## Output the user's input
# print("You entered:", user_input)

# 3.6.Using type(): You can directly call type(variable) to get the type of the variable.

# number = 10
# print(type(number))

# 4. Conditional Statements:
#  Python program to find greater and less than a number using if_else.
# age  = 20
# if age>=18:
#     print("Elegeble for voting")
# else:
#     print("not elegble for voting")

# Python program to check if a number is prime using if_else.

# for j in range (3,101):
#     n = j
#     flag = 0
#     for i in range (2,n):
#         if n%i==0:
#             flag = 1


        # if flag ==0:
        #     print(n,": prime")
        # else:
        #     pass

 # Python program to calculate grades based on percentage using if-else ladder.

# marks = int(input("Enter marks : "))

# if marks>=90 and marks<=100:
#     print("Grade A")
# elif marks>=70 and marks<90:
#     print("Grade B")
# elif marks>=50 and marks<70:
#     print("Grade C")
# elif marks>=35 and marks<50:
#     print("Grade D")
# elif marks>=0 and marks<35:
#     print("Grade F")
# else:
#     print("Invalid input : enter marks between 0 to 100")

#  Write a Python program to check if a person is eligible to donate blood using a nested if.

# age = int(input("enter your age : "))
#
# if age>=16:
#     if age==16:
#         print("we need your parental consent for donate blood")
#     else :
#         print("you are eligible to donate blood")
# else :
#     print("you are not eligible to donate blood")

# 5. Looping (For, While)

# : Write a Python program to print each fruit in a list using a simple for loop.

# list1=['apple','banana','mango']
# for i in list1:
#     print(i)

#2: Write a Python program to find the length of each string in List1.

# list1=['apple','banana','mango']
# for i in list1:
    # print(len(i))

 # 3 Write a Python program to find a specific string in the list using a simple for loop and if condition.
# List of strings

# fruits = ["apple", "banana", "orange"]
# string = "banana"
# for i in fruits:
#     if i == string:
#         print(f"Found the string: {i}")
#         break
# else:
    # print(f"The string '{string}' was not found in the list.")

#4: Print this pattern using nested for loop:

# *
# **
# ***
# ****
# *****

# lines=5
# stars=1
# for i in range(lines):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1

#6 Write a generator function that generates the first 10 even numbers.

# num=0
# for i in range(10):
#     num+=2
#     print(num)

# 7. Write a Python program to print "Hello" using a string.

# string="Hello"
# print(string)

#  Write a Python program to allocate a string to a variable and print it.

# string = "Hello, world!"
# print(string)

# 3) Write a Python program to print a string using triple quotes.

# print("""Sagar khodiyar""")

#  Write a Python program to access the first character of a string using index value.

# str = "Hello World"
# print(str[0])

# 5) Write a Python program to access the string from the second position onwards using slicing.

# str="Hello World"
# print(str[1:])

#  Write a Python program to access a string up to the fifth character.

# str = "Hello World"
# print(str[:5])

# Write a Python program to print the substring between index values 1 and 4.

# str = "Hello World"
# print(str[1:4])

# 8) Write a Python program to print a string from the last character.

# str = "Hello World"
# print(str[-1::-1])

# 9) Write a Python program to print every alternate character from the string starting from index 1.

# string = "Hello World"
# print(string[1::2])

# 1)Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

# list = ['apple', 'banana', 'mango']
# for fruit in list:
#     if fruit =='banana':
#         continue
#     print(fruit)

# 2) Write a Python program to stop the loop once 'banana' is found using the break statement.

# list = ['apple', 'banana', 'mango']
# for fruit in list:
#     if fruit =='banana':
#         break
#     print(fruit)

# Write a Python program to demonstrate string slicing.

# text = "My Name is Sagar"

# print("First five characters : ",text[:5])                       # Slicing from start to index 4
# print("Characters from index 2 to 6 : ",text[2:7])               # Slicing between specific indexes
# print("Last five characters : ",text[-5:])                       # Slicing last 5 characters
# print("String without first and last character : ",text[1:-1])   # Removing first and last character
# print("Every second character : ",text[::2])                     # Slicing with step size of 2
# print("Reversed string : ",text[-1::-1])                         # Reversing the string

# Write a Python program that manipulates and prints strings using various string methods.

# words = "My Name is Sagar"

# print(words.capitalize())
# print(words.casefold())
# print(len(words))
# print(words.center(41,'*'))
# print(words.count('a',0,7))
# print(words.endswith('m',0,9))
# print(words.find('k',3,9))
