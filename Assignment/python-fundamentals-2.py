# Program 1
'''
Write a program that takes salary as input.

Using conditional statements, calculate the tax based on the following rules:

1. If salary < 30,000 → Tax = 5%
2. If salary is between 30,000 and 70,000 (inclusive) → Tax = 15%
3. If salary > 70,000 → Tax = 25%

Print the final tax amount.
'''

# salary = int(input("Enter your salary for tax calculation : "))
# tax_amount = 0

# if (salary < 30000):
#     tax_amount = (salary * 0.05)
#     print("Your Tax Amount Is : ",tax_amount)
# elif (salary >= 30000 and salary <= 70000):
#     tax_amount = (salary * 0.15)
#     print("Your Tax Amount Is : ",tax_amount)
# else:
#     tax_amount = (salary * 0.25)
#     print("Your Tax Amount Is : ",tax_amount)

'''
------------------------------------------------------------------------------------------------
'''

# Program 2
# Write a function that takes two integers (start and end) and prints all the even numbers between them (inclusive).

# def even_number(a, b):
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i)

# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b : "))

# even_number(a,b)

'''
------------------------------------------------------------------------------------------------
'''

# Program 3
'''
Write a function that takes a number n and prints its digits
one by one.

For example:
If n = 312, the digits are:
3, 1, and 2.

Hint:
- The rightmost digit of a number can be obtained using:
  n % 10
- To remove the rightmost digit, use:
  n = n // 10
'''

# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10 

# number = int(input("enter number here : "))
# print_digits(number)

'''
------------------------------------------------------------------------------------------------
'''

# Program 4
# Write a function to return the count the number of digits in a number, n.

# def count_digits(n):
#     count = 0

#     while n > 0:
#         count += 1
#         n = n // 10

#     return count

# n = int(input("Enter value for number n to count its digits : "))

# print(count_digits(n))

'''
------------------------------------------------------------------------------------------------
'''

# Program 5
# Write a function to return the of a number, sum of digits n.

# def sum_of_digits(n):
#     sum = 0

#     while n > 0:
#         digit = n % 10
#         n = n // 10
#         sum += digit

#     return sum

# n = int(input("Enter value for number n to sum its digits : "))
# print(sum_of_digits(n))

'''
------------------------------------------------------------------------------------------------
'''

# Program 6
# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

# for i in range(1,101):
#     if (i % 3 == 0 and i % 5 == 0):
#         print(i)

'''
------------------------------------------------------------------------------------------------
'''

# Program 7
'''
Design a program to continuously take input from the user
and print whether the entered number is positive or negative.

Keep accepting input until the user enters "Quit",
then terminate the program.
'''

# while True:
#     n = input("Enter input number or Quit : ")

#     if (n == "Quit"):
#         break

#     n = int(n)
#     if (n >= 0):
#         print("Positive")
#     else:
#         print("Negative")

'''
------------------------------------------------------------------------------------------------
'''

# Program 8
'''
Create a simple calculator using a function:

calculator(a, b, operation)

The function should perform the arithmetic operation
based on the value of the 'operation' parameter.

Supported operations:
1. '+' → Addition
2. '-' → Subtraction
3. '*' → Multiplication
4. '/' → Division

Display the result of the selected operation.
'''

# def calculator(a, b, operation):
#     if (operation == '+'):
#         return a + b
#     elif (operation == '-'):
#         return a - b
#     elif (operation == '*'):
#         return a * b
#     elif (operation == '/'):
#         return a / b
    
# operation = input("Enter which operation you want to perform : ")
# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b : "))

# print(calculator(a, b, operation))

'''
------------------------------------------------------------------------------------------------
'''

# Program 9
'''
Write a function:

is_prime(n)

The function should return:
- True, if n is a prime number.
- False, otherwise.

A prime number is a number greater than 1 that has
exactly two factors: 1 and itself.

Hint:
- Check divisibility for numbers from 2 to n - 1.
- If n is divisible by any number in this range,
  it is not a prime number.
- Otherwise, it is a prime number.
'''

# def is_prime(n):

#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# n = int(input("Enter your number: "))

# if is_prime(n):
#     print(f"{n} is a Prime Number")
# else:
#     print(f"{n} is Not a Prime Number")

'''
------------------------------------------------------------------------------------------------
'''

# Program 10
'''
Create a "Number Guessing Game".

Choose a secret number in the program and ask the user
to guess it.

Print:
- "Too High" if the guess is greater than the secret number.
- "Too Low" if the guess is less than the secret number.
- "Correct!" if the guess matches the secret number.
'''


# while True:
#     secret_number = 55

#     guess_number = int(input("Enter your gussed number : "))

#     if guess_number < secret_number:
#         print("Too Low")
#     elif guess_number > secret_number:
#         print("Too High")
#     else:
#         print("Correct")
#         break


