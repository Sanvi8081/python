# PYTHON 
Learning Python step by step with daily GitHub commits....

# Day 1: Variables & Data Types 🐍

This folder contains basic Python examples to understand variables and built-in data types.

## Topics Covered

* Variables
* Integer, Float
* String
* Boolean


## Files

* `variables_and_datatypes.py` – Simple examples of Python data types.



# Day 2 : Python Conditional Statements 🐍
Conditional-Statements/
│
├── grade_system.py
│   └── if-elif-else grade calculation
│
├── ternary_operator.py
│   └── single-line if / ternary examples
│
├── salary_tax.py
│   └── clever conditional tax calculation
│
└── README.md
    └── project description and concepts covered

## Topics Covered

if-elif-else conditional statements

Single-line if (ternary operator)

clever if (ternary operator)

### Code Overview
1. Grade System

Assigns grades to a student based on marks obtained.

2. Ternary Operator Examples

Checks if the subject is accounts

Prints results using single-line conditional expressions

3. Salary Tax Calculation

Calculates tax based on salary using a compact conditional expression:

10% tax for salary ≤ 50,000

20% tax for salary > 50,000




## files
* `conditional_statements.py` –  examples of Python conditional statements.

## Day 3: Operators & Type Conversion 🐍

This folder contains basic Python examples to understand operators and type conversion.

## Topics Covered

Arithmetic Operators (+, -, *, /)

Assignment Operators

Comparison Operators

Logical Operators

Type Conversion

int(), float(), str()

Practice Programs 🧠💻
Practice Program 1: Sum of Two Numbers
Practice Program 2: Area of a Square


# Day 4: String Functions 🐍

This day focuses on understanding **Python strings** and commonly used **string methods**.

## Topics Covered
- String basics
- `endswith()`
- `capitalize()`
- `replace()`
- `find()`
- `count()`
- String formatting

## Practice
- Check string endings
- Modify and replace words
- Find characters in a string
- Count word occurrences

📌 These concepts help in text processing and data handling in Python.

## Day 5: Lists & Tuples 🐍
📌 Overview

Learned how to work with Lists and Tuples in Python, including slicing, methods, and basic problem-solving.

## Topics Covered
Lists

List creation

List slicing (positive & negative indexing)

append()

insert()

reverse()

sort() (ascending & descending)

Copying lists

Tuples

Tuple creation

count() method

Immutable nature of tuples

🧪 Practice

Performed list slicing on fruits list

Used list methods (append, insert, reverse, sort)

Took user input and stored values in a list

Checked if a list is a palindrome

Counted occurrences of "A" grade in a tuple

💡 Key Takeaways

Lists are mutable (can be changed).

Tuples are immutable (cannot be changed).

sort() works only with lists.

count() works with both lists and tuples

## Day 6: Sets 🐍
📌 Overview

Learned how to work with Sets in Python, including set creation, set methods, and set operations like union and intersection.

📚 Topics Covered
🔹 Set Basics

Creating a set using { }

Removing duplicate values automatically

Checking the type using type()

Creating an empty set using set()

🔹 Set Methods

add() → Add an element

remove() → Remove a specific element

pop() → Remove a random element

clear() → Remove all elements

🔹 Set Operations

union() → Combine two sets

intersection() → Find common elements

🔹 Special Case Practice

Storing 9 and 9.0 separately in a set

Using built-in data types (tuples) to differentiate values


## Day 7: For Loop 🔁🐍

📌 Overview
Learned how to use for loops in Python to iterate over sequences like lists and ranges, including for-else, range(), and pass.

📚 Topics Covered

🔹 For Loop Basics

Used to iterate over lists, tuples, strings, etc.

Executes a block of code for each element.

🔹 For Loop with else

else runs after the loop finishes normally.

Does not run if loop is stopped using break.

🔹 Using range()

Generates a sequence of numbers.

range(n) → 0 to n-1

range(start, stop, step) can customize the sequence.

🔹 pass Statement

Placeholder statement.

Used when a loop is required but no action is needed.

🔹 Practice Problems

Sum of first n numbers (using while)

Factorial of n (using for)

🎯 Key Points

✔ for loop is used for iteration
✔ Works with sequences (list, range, string, etc.)
✔ else runs after normal loop completion
✔ range() helps generate number sequences
✔ pass does nothing (used as placeholder)

📌 Overview
Learned how to use while loops to repeat code as long as a condition is True.

📚 Topics Covered

🔹 While Loop Basics

Runs while condition is True

Condition checked before each iteration

🔹 Printing Numbers

1 to 100

100 to 1

🔹 Multiplication Table

Printed table of a number using while

🔹 Traversing List/Tuple

Used index with len() to access elements

🔹 break and continue

break → Stops loop

continue → Skips one iteration

🎯 Key Points

✔ Used when iterations are condition-based
✔ Must update variable to avoid infinite loop
✔ Can be used for searching and counting
✔ break and continue control loop flow

## Day 8 – Python Functions (Short README)
🔹 Overview

This program demonstrates the basics of Python functions, including function definition, parameters, return values, default arguments, and simple practice problems like factorial, list handling, and number evaluation.

🔹 Concepts Covered

Function Definition (def)

Function Call & Arguments

Parameters vs Arguments

Return Statement

Built-in vs User-defined Functions

Default Parameters

Loops inside Functions

Basic Problem Solving using Functions

🔹 Functions Implemented

calcsum(a, b, c)
Calculates and prints the sum of three numbers.

avg(a, b, c)
Computes the average of three numbers.

cal_prod(a=1, b=1)
Demonstrates default parameters by multiplying two numbers (default = 1).

print_len(cities)
Prints the length of a list.

print_list(list)
Prints all elements of a list in a single line.

cal_fact(n)
Calculates the factorial of a given number using a loop.

converter(usd_val)
Converts USD to INR using a fixed conversion rate.

evaluator(n)
Checks whether a number is odd or even.

🔹 Built-in Functions Used

print()

len()

range()

type()

🔹 Key Learnings

Functions help in code reusability and modularity.

Parameters allow passing data to functions.

Return values make functions reusable in larger programs.

Default parameters prevent errors when arguments are not passed.

Functions can be used to solve real-world problems like conversions, factorial, and evaluations.

## Day 9 – Recursion in Python 

This project covers the basics of recursion in Python using simple examples like printing numbers, factorial calculation, sum of natural numbers, and recursive list traversal. It focuses on understanding base cases and recursive function calls.

🧠 Concepts Covered

Recursion

Base Case & Recursive Calls

Factorial using Recursion

Sum of First N Natural Numbers

List Traversal using Recursion

🛠️ Implemented Functions

show(n) → Prints numbers from n to 1 recursively

fact(n) → Calculates factorial of a number

sum(n) → Finds sum of first n natural numbers

print_list(list, idx=0) → Prints list elements recursively


##  DAY 10 Python File Handling (Basic Practice)
📌 Overview

This project demonstrates basic File I/O operations in Python including reading, writing, replacing text, and searching content inside files. It is a beginner-friendly practice script to understand how file handling works.

🛠️ Features

Read file content (read, readline)

Write and overwrite files (w, r+ modes)

Use with statement for safe file handling

Replace text in a file (Java → Python)

Search a word in a file

Create and manage text files

🧠 Concepts Covered

File modes: r, w, r+

Text manipulation using replace()

Word searching using find()

Automatic file closing with with

🎯 Purpose

Built for practice to strengthen fundamentals of Python file handling and understand real-world file operations in a simple way.

## DAY 11 🐍 Python OOP Basics – Classes & Constructors

This repository contains beginner-friendly examples of Object-Oriented Programming (OOP) in Python using classes, objects, and constructors.

📌 Major Concepts Covered

Class and Object creation

Class attributes

Constructor (__init__)

Parameterized constructor

Instance variables using self

💡 Description

The code demonstrates:

Creating a Student class and accessing its attribute through an object

Defining a Car class with multiple attributes

Using a parameterized constructor in the Teacher class to initialize object data automatically when an object is created

🧠 Key Learning

Classes act as blueprints for objects

Objects store data using instance variables

__init__() initializes values during object creation

self refers to the current instance of the class






