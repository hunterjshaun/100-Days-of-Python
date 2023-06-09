### Code Challenge: Odd or Even 
# Determine whether a number is even or odd
# % (Modulo) - In Python, the modulo operator % returns the remainder of dividing two numbers.
# Even numbers can be divided by 2 with no remainder

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

### Code Challenge BMI calculator 2.0
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# you should round the result to the nearest whole number.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = round(float(weight) / float(height) ** 2)

if BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
elif BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > round(18.5) and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")


### Code Challenge Leap year calculator
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 == 0:
    print("Not leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
else:
    print("Not leap year.")