# 0x07. Python - Test-driven development
Foundations - Higher-level programming ― Python

By Guillaume, CTO at Holberton School

[Carlos Andres Polania](https://twitter.com/timberdev) (capolaniaq@correo.udistrital.edu.co)

## Learning Objectives
-   Why Python programming is awesome
-   What’s an interactive test
-   Why tests are important
-   How to write Docstrings to create tests
-   How to write documentation for each module and function
-   What are the basic option flags to create tests
-   How to find edge cases

## Tasks
### 0. add_number
Write a function that adds 2 integers.
-   Prototype:  `def add_integer(a, b=98):`
-   `a`  and  `b`  must be integers or floats, otherwise raise a  `TypeError`  exception with the message  `a must be an integer`  or  `b must be an integer`
-   `a`  and  `b`  must be first casted to integers if they are float
-   Returns an integer: the addition of  `a`  and  `b`
-   You are not allowed to import any module

### 1. Divide a matrix
Write a function that divides all elements of a matrix.
-   Prototype:  `def matrix_divided(matrix, div):`

### 2. Say my name
Write a function that prints `My name is <first name> <last name>`
-   Prototype:  `def say_my_name(first_name, last_name=""):`
-   `first_name`  and  `last_name`  must be strings otherwise, raise a  `TypeError`  exception with the message  `first_name must be a string`  or  `last_name must be a string`
-   You are not allowed to import any module

### 3. Print square
Write a function that prints a square with the character `#`
-   Prototype:  `def print_square(size):`

### 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
-   Prototype:  `def text_indentation(text):`

### 5. Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function  `def max_integer(list=[]):`.

### 6. Matrix multiplication
Write a function that multiplies 2 matrices:

-   Read:  [Matrix multiplication - only Matrix product (two matrices)](https://intranet.hbtn.io/rltoken/gG3TcWESGFqiZzHNlMbEKA "Matrix multiplication - only Matrix product (two matrices)")

-   Prototype:  `def matrix_mul(m_a, m_b):`