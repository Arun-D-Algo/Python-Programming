#Program to make a simple MATHEMATICS CALCULATOR with addition, subtraction, multiplication, division, square rooting, 

import math 

def menu():
    print("""
1 : Add N numbers
2: Subtract two numbers
3: Mutliply N numbers
4: Divide two numbers 
5: Square a number
6: Cube a number
7: Raise a number to Power n
8: Square root of a number
9: Logarithm of a number
10: Quadratic Roots of a quadratic expression
0: Exit""")









def add(nums):
    return sum(nums)

def subtract(num):
    

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
operator = input("Enter any operator : ")

match operator:
    case "+":
        sum = add(a,b)
        print(sum)

    case "-":
        difference = subtract(a,b)
        print(difference)

    case "*":
        product = multiply(a,b)
        print(product)

    case "/":
        qoutient = divide(a,b)
        print(qoutient)
    

        