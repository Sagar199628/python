# 1. Introduction to Python:
#
#     1. Introduction to Python and its Features (simple, high-level, interpreted language).
#     * python syntex is clean, simple,& easy language.
#     * it is high level language.
#     * python excute code line by line.
#
#     2.  History and evolution of Python.
#     * python was created by guido van rossum in late of 1980s officially released in 1991.
#     * it is designed to be simple, readable, and powerful programming language.
#
#     3.  Advantages of using Python over other programming languages.
#     * easy to learn and use.
#     * high-level and interpriter language.
#     * extensive laibraries .
#     * object orianted and functional programming.
#
# 2. Programming Style :
#
#    1. Understanding Python’s PEP 8 guidelines.
#    indentation : 4 space
#
#    2. Indentation, comments, and naming conventions in Python.
#     * indentation : here we have to use 4 space insted of tab
#     * comments : comments are define by #
#     * naming : in python we can not use keyword name as variable name and variable name can not start with number
#                we can use numbers and _ in variable name.
#
#    3. Writing readable and maintainable code.
#     code :  a=10
#             b=20
#             Sub=a-b
#             print(sub)
#
# 3. Core Python Concepts:
#
#     1. Understanding data types: integers, floats, strings, lists, tuples, dictionaries, sets.
#
#     * numeric type : int, float, complex
#     * text type : str
#     * sequence type : list, tuple, range
#     * mapping type : dict
#     * set type : set, frozenset
#     * boolen type : boolen
#     * none type : none
#
#     2. Python variables and memory allocation.
#
#     * variables name rules : Variable names can contain letters, digits, and underscores (_).
#     * Variable names must not start with a digit.
#     * Python is case-sensitive, so a and A would be different variables.
#
#     3. Python operators: arithmetic, comparison, logical, bitwise.
#
#     * arithmetic : +,-,*,/,%,**,//
#     * comparison : ==,!=,>,<,>=,<=
#     * logical : and,or,not
#     * bitwise : &,|,^,~,>>,<<
#
# 4. 4. Conditional Statements
# Introduction to conditional statements: if, else, elif.
#
#     if condition:
#         # Code to execute if condition is true
#
#     if condition:
#         # Code to execute if condition is true
#     else:
#         # Code to execute if condition is false
#
#     if condition1:
#         # Code to execute if condition1 is true
#     elif condition2:
#         # Code to execute if condition2 is true
#     else:
#         # Code to execute if none of the conditions are true
#
# Nested if-else conditions.
#
# if condition1:
#     if condition2:
#         # Code to execute if condition1 and condition2 are True
#     else:
#         # Code to execute if condition1 is True and condition2 is False
# else:
#     # Code to execute if condition1 is False
#
# 5. Looping(For, While)
#
# 1. Introduction to for and while loops.
#
#     for loop : when we know that how many times we have to run the loop
#         example : we have to print 1 to 5 numbers
#             code : for i in range(1,6):
#                         print(i)
#
#     while : when we have to run the loop till the condition is not satisfied
#         example : we have to print 1 to 5 number
#             code : i=1
#                    while i<=5:
#                    print(i)
#
#
#     2. Using loops with collections (lists, tuples, etc.).
#
#     list=["apple","banana","cherry"]
#     for i in list:
#         print(i)
#
#     tuples=("apple","banana","cherry")
#     for i in tuples:
#         print(i)
#
# 7. Functions and Methods
#
#   1.In Python, functions are defined using the def keyword, followed by the function name,
#     parentheses () for any parameters (optional), and a colon : to start the function body.
#
#     In Python, methods are functions that are associated with an object.
#     They are defined within a class and can be called on an instance of that class (an object).
#     Methods are like functions, but they always take at least one argument: self.
#     This self refers to the instance of the object itself
#
#     * Instance Methods: Use self to work with instance-specific data.
#
#     *  Class Methods: Use cls to work with class-specific data.
#
#     *  Static Methods: Do not use self or cls, just regular parameters.
#
#   2.In Python, function arguments can be passed in different ways,
#     such as positional arguments, keyword arguments, and default arguments.
#
#   3.Built-in methods for strings, lists, etc.