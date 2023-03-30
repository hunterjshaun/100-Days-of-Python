### Loops
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


### Code challenge: Average Height using for loops
# This code block is a for loop that iterates over each index in the list `student_heights`.
# The `range()` function generates a sequence of integers from 0 up to, but not including, 
# the length of the `student_heights` list.
# For each index in the `student_heights` list, we access the corresponding element using 
# square brackets notation (`student_heights[n]`), convert the value to an integer using the 
# `int()` function, and assign it back to the same element in the list.
# The end result is that each element in the `student_heights` list is converted from a 
# string to an integer, which makes it easier to perform mathematical operations or comparisons
# on the heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # turning the student heights into integers
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total = 0 # creating a variable so the heights can be added to it
for height in student_heights:
    total += height
average = total / len(student_heights)
print(average) 


### Code challenge: Max value from a list using for loops
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
highest = 0
for h in student_scores:
    if h > highest:
        highest = h

print(f"The highest score in the class is: {highest}")
