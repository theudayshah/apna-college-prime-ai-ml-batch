# Program 1
# Write a program that asks the user for their name and age, then prints a sentence

# name = input("Enter Your Name :")
# age = int(input(f"Enter Your Age {name}: "))

# print("Hello", name, "your age is", age)

'''
------------------------------------------------------------------------------------------------
'''


# Program 2
# Take two numbers as input from the user and print their sum, difference, product, and quotient

# num1 = int(input("Enter Value of Num1 :"))
# num2 = int(input("Enter Value of Num2 :"))

# sum = num1 + num2
# difference = num1 - num2
# product = num1 * num2
# quotient = num1 / num2

# print(f"Sum of two numbers is {sum} \nDifference of two numbers is {difference} \nProduct of two numbers is {product} \nQuetiont of two numbers is {quotient}")


'''
------------------------------------------------------------------------------------------------
'''

# Program 3
# Ask the user to enter two integers and one float.Convert them all to floats and print their average

# num1 = int(input("Enter Value of Num1 (Integer) :"))
# num2 = int(input("Enter Value of Num2 (Integer) :"))
# num3 = float(input("Enter Value of Num3 (Float) :"))

# num1 = float(num1)
# num2 = float(num2)

# average = ( num1 + num2 + num3 ) / 3

# print(f"average of {num1}, {num2}, {num3} is {average}")

'''
------------------------------------------------------------------------------------------------
'''

# Program 4
'''
The user enters a string containing a number (e.g., "45").
Convert it to:
1. An integer
2. A float
3. A string again
Print all three values along with their data types.
'''

# str_num = input("enter any number (it must be interger number)")

# str_num = int(str_num)
# print(str_num)
# print(type(str_num))

# str_num = float(str_num)
# print(str_num)
# print(type(str_num))

# str_num = str(str_num)
# print(str_num)
# print(type(str_num))

'''
------------------------------------------------------------------------------------------------
'''

# Program 5
'''
Evaluate and print the result of the following expression:

x = 10 + 3 * 2 ** 2

Based on what you learned in the lecture,
explain why the output is what it is.
'''

# x = 10 + 3 * 2 ** 2
# print(x)

# answer = "The output is 22 because Python follows operator precedence. First 2 ** 2 is evaluated to 4, then 3 * 4 becomes 12, and finally 10 + 12 gives 22."
# print(answer)

'''
------------------------------------------------------------------------------------------------
'''

# Program 6
# Write a program to swap values of two numbers entered by the user.

# num1 = int(input("enter num1 :"))
# num2 = int(input("enter num2 :"))

# print(f"before swapping numbers num1 is {num1} and num2 is {num2}")

# print("-----swapping-----")

# temp = num1
# num1 = num2
# num2 = temp

# print(f"after swapping numbers num1 is {num1} and num2 is {num2}")

'''
------------------------------------------------------------------------------------------------
'''

# Program 7
'''
Ask the user for a temperature in Celsius (string input).
Convert it to a float, then calculate and print the
temperature in Fahrenheit.

Conversion Formula:
FahrenheitTemp = (CelsiusTemp * (9 / 5)) + 32
'''

# CelsiusTemp = input("Enter Current Temperature Here In Celsius : ")
# temperature = float(CelsiusTemp)

# FahrenheitTemp = (temperature * (9 / 5)) + 32
# print(f"Your Current Temperature in Fahrenheit is : {FahrenheitTemp}")

'''
------------------------------------------------------------------------------------------------
'''

# Program 8
'''
Take the radius (r) as user input and print the area of the circle.

Use the formula:
Area = π * r²

Assume the value of π = 3.14
'''

# PI = 3.14

# radius = float(input("Enter Radius of Circle Here : "))

# area = PI * radius ** 2

# print(f"Area of Circle for Given Radius Is : {area}")

'''
------------------------------------------------------------------------------------------------
'''

# Program 9
'''
Ask the user for:
1. Principal (P)
2. Rate (R)
3. Time (T)

Convert all inputs to float and compute the Simple Interest (SI).

Formula:
SI = (P * R * T) / 100
'''

# Principal = float(input("Enter Principal Amount : "))
# Rate = float(input("Enter Rate of Interest : "))
# Time = float(input("Enter Time in Years : "))

# simpleInterest = (Principal * Rate * Time) / 100

# print(f"Your Simple Interest Value is : {simpleInterest}")
# print(f"Your Principal Amount is : {Principal}")
# print(f"Your Interest Rate is : {Rate}%")
# print(f"Your TIme in Years is : {Time} years")

'''
------------------------------------------------------------------------------------------------
'''

# Program 10
'''
Take a decimal number as input (e.g., 45.78) and output its:
1. Integer part (e.g., 45)
2. Fractional part (e.g., 0.78)
'''

# number = float(input("Enter Float Number Here : "))

# integerPart = int(number)
# fractionalPart = number - integerPart

# print(f"Integer Part is {integerPart}")
# print(f"Fractional Part is {fractionalPart}")

'''
------------------------------------------------------------------------------------------------
'''
