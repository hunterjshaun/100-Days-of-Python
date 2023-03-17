### Data types

### String

### Indexing
# print("hello"[0])


### Integer - whole number

# print(123 + 345)

# print(1_233 + 4_000)


### Float - floating pont number

# 3.14159

### Boolean - True or False

###

# num_char = len(input("what is your name? "))
# print(type(num_char))


### Code Challenge add a 2 digit number by itself.
# two_digit_number = input("Type a two digit number: ")
# two_digit_add = int(two_digit_number[0]) + int(two_digit_number[1])
# print(two_digit_add)

### Code Challenge BMI calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# BMI = float(weight) / float(height) ** 2
# print(int(BMI))

### Code challenge How long you have to live
age = input("What is your current age? ")
age_int = int(age)
days_year = 365
weeks_year = 52
months_year = 12

days_left = (90 - age_int) * 365
weeks_left = (90 - age_int) * 52
months_left = (90 - age_int) * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")